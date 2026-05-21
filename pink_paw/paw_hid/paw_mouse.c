#include <stdbool.h>
#include <stdint.h>

#include "bsp/board_api.h"
#include "pico/stdlib.h"
#include "tusb.h"
#include "class/hid/hid_device.h"

#define PIN_BUTTON 2

#define PIN_RIGHT  4
#define PIN_LEFT   5
#define PIN_DOWN   7
#define PIN_UP     8

#define MOVE_STEP  2 //adjust for paw speed

static void init_input(uint pin)
{
    gpio_init(pin);
    gpio_set_dir(pin, GPIO_IN);
    gpio_pull_up(pin);
}

static bool active(uint pin)
{
    return gpio_get(pin) == 0; // active-low: pad/button connects to GND
}

int main(void)
{
    board_init();
    tusb_init();

    init_input(PIN_BUTTON);
    init_input(PIN_UP);
    init_input(PIN_DOWN);
    init_input(PIN_LEFT);
    init_input(PIN_RIGHT);

    while (true) {
        tud_task();

        if (!tud_hid_ready())
            continue;

        int8_t dx = 0;
        int8_t dy = 0;
        uint8_t buttons = 0;

        if (active(PIN_LEFT))
            dx -= MOVE_STEP;
        if (active(PIN_RIGHT))
            dx += MOVE_STEP;

        if (active(PIN_UP))
            dy -= MOVE_STEP;
        if (active(PIN_DOWN))
            dy += MOVE_STEP;

        if (active(PIN_BUTTON))
            buttons |= MOUSE_BUTTON_LEFT;

        tud_hid_mouse_report(
            0,       // report ID
            buttons,
            dx,
            dy,
            0,       // vertical wheel
            0        // horizontal wheel / pan
        );

        sleep_ms(10); //adjust for paw speed
    }
}
