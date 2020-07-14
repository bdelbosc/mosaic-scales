#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import OrderedDict

import matplotlib.patches as patches
from matplotlib.pyplot import subplots

dpi = 600

chrom = OrderedDict([
    ('do4', {"finger": 0, "octave": 4, "note_fr": "do", "note_en": "C"}),
    ('do4#', {"finger": 123, "alt": "re4b"}),
    ('re4', {"finger": 123}),
]
)

finger_codec = {None: [],
                0: [False, False, False],
                123: [True, True, True],
                13: [True, False, True],
                23: [False, True, True],
                12: [True, True, False],
                1: [True, False, False],
                2: [False, True, False],
                3: [False, False, True]}

chromatic = [123, 13, 23, 12, 1, 2, 0, 123, 13, 23, 12, 1, 2, 0, 23, 12, 1, 2, 0, 12, 1, 2, 0, 1, 2, 0, 23, 12, 1, 2, 0,
             12, 1, 2, 0, 1, 2, 0]
names = ["Fa#", "Sol", "Lab", "La", "Sib", "Si",
         "Do", "Do#", "Ré", "Ré#", "Mi", "Fa", "Fa#", "Sol", "Lab", "La", "Sib", "Si",
         "Do", "Do#", "Ré", "Ré#", "Mi", "Fa", "Fa#", "Sol", "Lab", "La", "Sib", "Si",
         "Do", "Do#", "Ré", "Ré#", "Mi", "Fa", "Fa#", "Sol"]

major_interval = (2, 2, 1, 2, 2, 2, 1)
minor_mel_interval = (2, 1, 2, 2, 2, 2, 1)
minor_nat_interval = (2, 1, 2, 2, 1, 2, 2)
minor_har_interval = (2, 1, 2, 2, 1, 3, 1)
arpeggio_interval = (4, 3, 5)
arpeggio_dec_interval = (2, 3, 2, 4, 1)
diminushed_interval = (2, 1, 2, 1, 2, 1, 2, 1)
tons = [False, True, False, True, False, True, True, False, True, False, True, True, False, True, False, True, False,
        True, True,
        False, True, False, True, True, False, True, False, True, False, True, True, False, True, False, True, True,
        False, True]

step = 1
space = 0.075


def get_scale(interval, start, nb_octave=1):
    ret = [None] * len(chromatic)
    indice = start
    ret[indice] = chromatic[indice]
    for int in interval * nb_octave:
        indice += int
        ret[indice] = chromatic[indice]
    return ret


def draw_note(ax, y, f, color):
    if f:
        for digit in [0, 1, 2]:
            ax.add_patch(
                patches.Rectangle(
                    (step * digit + space, y + space),
                    step - 2 * space,
                    step - 2 * space,
                    fill=f[digit],
                    edgecolor='black',
                    facecolor=color,
                    linewidth=0.25
                )
            )


def draw_scale(ax, scale, color='black'):
    y = len(scale) - 1
    i = 0
    for note in scale:
        if tons[i]:
            c = 'gray'
        else:
            c = 'black'
        draw_note(ax, y, finger_codec[note], c)
        y = y - step
        i += 1


def adapt(ax, title=None):
    ax.set_ylim(0, len(chromatic))
    ax.set_xlim((0, 3))
    ax.set_aspect(1)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    if title:
        ax.set_title("C5#", fontsize=4)


def all_majors():
    fig, axs = subplots(1, 14, figsize=(3.5, 4), dpi=dpi, facecolor='w', sharey=True)
    fig.suptitle("Major Scales", fontsize=7)
    fig.subplots_adjust(top=2.3)
    for ax in axs:
        adapt(ax)
    draw_scale(axs[0], chromatic)
    g = 1
    for i in [0, 2, 4, 6, 8, 10, 12, -1, 1, 3, 5, 7, 9]:
        axs[g].set_title(names[6 + i], fontsize=5)
        draw_scale(axs[g], get_scale(major_interval, 6 + i))
        g += 1
    fig.savefig("major-scales-1.png", bbox_inches='tight')


def all_majors_quinte():
    fig, axs = subplots(1, 14, figsize=(3.5, 4), dpi=dpi, facecolor='w', sharey=True)
    fig.suptitle("Major Scales", fontsize=7)
    fig.subplots_adjust(top=2.3)
    for ax in axs:
        adapt(ax)
    draw_scale(axs[0], chromatic)
    g = 1
    for i in [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]:
        axs[g].set_title(names[6 + i], fontsize=5)
        draw_scale(axs[g], get_scale(major_interval, 6 + i))
        g += 1
    fig.savefig("major-scales-2.png", bbox_inches='tight')


def all_majors_quinte_double():
    fig, axs = subplots(1, 14, figsize=(3.5, 4), dpi=dpi, facecolor='w', sharey=True)
    fig.suptitle("Major Scales", fontsize=7)
    fig.subplots_adjust(top=2.3)
    for ax in axs:
        adapt(ax)
    draw_scale(axs[0], chromatic)
    g = 1
    # for i in [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]:
    for i in [0, -5, 2, -3, 4, -1, -6, 1, -4, 3, -2, 5]:
        axs[g].set_title(names[6 + i], fontsize=5)
        draw_scale(axs[g], get_scale(major_interval, 6 + i, 2))
        g += 1
    fig.savefig("major-scales-2-octaves.png", bbox_inches='tight')


def all_minors():
    fig, axs = subplots(1, 27, figsize=(7, 4), dpi=dpi, facecolor='w', sharey=True)
    fig.suptitle("Minor Scales Melodic / Pure", fontsize=7)
    fig.subplots_adjust(top=2.3)
    for ax in axs:
        adapt(ax)
    draw_scale(axs[0], chromatic)
    g = 1
    for i in [0, 2, 4, 6, 8, 10, 12, -1, 1, 3, 5, 7, 9]:
        axs[g].set_title(names[6 + i], fontsize=6)
        draw_scale(axs[g], get_scale(minor_mel_interval, 6 + i))
        if i == 12:
            draw_scale(axs[g + 1], get_scale(minor_nat_interval, 6 + i - 12, 2))
        else:
            draw_scale(axs[g + 1], get_scale(minor_nat_interval, 6 + i))
        g += 2
    fig.savefig("minor-scales.png", bbox_inches='tight')


def diminushed_scale():
    fig, axs = subplots(1, 3, figsize=(1.5, 4), dpi=dpi, facecolor='w', sharey=True)
    fig.suptitle("Diminushed Scales", fontsize=7)
    fig.subplots_adjust(top=3)
    for ax in axs:
        adapt(ax)
    draw_scale(axs[0], chromatic)
    g = 1
    for i in [0, 1]:
        axs[g].set_title(names[6 + i], fontsize=6)
        draw_scale(axs[g], get_scale(diminushed_interval, 6 + i, 2))
        g += 1
    fig.savefig('diminushed-scales.png', bbox_inches='tight')


def arpeggios():
    fig, axs = subplots(1, 27, figsize=(7, 4), dpi=dpi, facecolor='w', sharey=True)
    fig.suptitle("Arpeggios", fontsize=7)
    fig.subplots_adjust(top=2.3)
    for ax in axs:
        adapt(ax)
    draw_scale(axs[0], chromatic)
    g = 1
    for i in [0, 2, 4, 6, 8, 10, 12, -1, 1, 3, 5, 7, 9]:
        # for i in [0,4,8,12,-1,3,7,11]:
        axs[g].set_title(names[6 + i], fontsize=6)
        draw_scale(axs[g], get_scale(arpeggio_interval, 6 + i))
        if i == 12:
            draw_scale(axs[g + 1], get_scale(arpeggio_dec_interval, 6 + i - 12, 2))
        else:
            draw_scale(axs[g + 1], get_scale(arpeggio_dec_interval, 6 + i))
        g += 2
    fig.savefig("arpeggios.png", bbox_inches='tight')


all_majors_quinte_double()
all_majors_quinte()
all_majors()
all_minors()
arpeggios()
diminushed_scale()
