# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

'''
Módulo actores
==============

Este módulo representa a los actores del juego:

    * :Jugador1: barra roja ubicada a la izquierda y comandada por las teclas <W> (arriba) y <S> (abajo).
    * :Jugador2: barra azul ubicada a la derecha y comandada por las teclas direccionales <arriba> y <abajo>.
    * :Pelota: bomba que representa la pelota. Esta explotará al terminar el juego.
    * :Puntaje1: puntaje correspondiente al Jugador 1.
    * :Puntaje2: puntaje correspondiente al Jugador 2.

'''

from jugador_1_rojo import Jugador1
from jugador_2_azul import Jugador2
from pelota import Pelota
from puntajes import Puntaje1, Puntaje2
