#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: Sep 2019
# This program draws a background on the PyBadge

import ugame
import stage
import constants


def main():
    # this function sets the background

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # a list of sprites that will be updated every frame
    sprites = []

    # parameters (image_bank_1, image # in bank, x, y)
    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / 2 -
                        constants.SPRITE_SIZE / 2), int(constants.SCREEN_Y -
                        constants.SPRITE_SIZE + constants.SPRITE_SIZE / 2))
    sprites.append(ship)  # insert at top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the background layer
    game.layers = sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # get user inputs
        keys = ugame.buttons.get_pressed()

        # print(keys)
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_UP != 0:
            if ship.y < 0:
                ship.move(ship.x, 0)
            else:
                ship.move(ship.x, ship.y - 1)
            pass
        if keys & ugame.K_DOWN != 0:
            if ship.y > constants.SCREEN_Y - constants.SCREEN_GRID_Y:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
            else:
                ship.move(ship.x, ship.y + 1)
            pass
        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SCREEN_GRID_X:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE,
                          ship.y)
            else:
                ship.move(ship.x + 1, ship.y)
            pass
        # update game logic
        # play sound if A is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()