#!/bin/python
##############################################################################
#
#          FILE:  aangifte.py
#
#         USAGE:  ./aangifte.py
#   DESCRIPTION:  Prints a possible reason to accuse someone based on a
#                 random crime (accusation) and a random noun, with often
#                 hilarious results.
#                 I'm in the process of learning Python, so this is probably
#                 quite ugly.
#       OPTIONS:  None
#  REQUIREMENTS:  python, random
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Dennis van Zuijlekom, dvanzuijlekom@hack42.nl
#       COMPANY:  Hackerspace Hack42 Arnhem
#       VERSION:  1.1
#       CREATED:  2014-04-15
#      REVISION:  ---
##############################################################################
#       CHANGES:  2014-04-15, DVZ, 1.0
#                 Initial release.
#                 2014-04-22, DVZ, 1.1
#                 Added a few accusations and nouns
##############################################################################

import random

accusation = []
accusation.append("het mishandelen van")
accusation.append("obscene gedragingen met")
accusation.append("openbare schennispleging met")
accusation.append("verboden bezit van")
accusation.append("het slaktofferen van")
accusation.append("vervalsing van")
accusation.append("valsheid in geschrifte met behulp van")
accusation.append("het in een openbare ruimte onder invloed zijn van")
accusation.append("het zonder vergunning bedienen van")
accusation.append("het negeren van bord C.21, verbod op")
accusation.append("het na 22:00 's avonds geluidsoverlast veroorzaken met")
accusation.append("het inwendig smokkelen van")
accusation.append("belediging van")
accusation.append("verstoring van de openbare orde, gebruikmakend van")
accusation.append("onrechtmatig gebruik van")
accusation.append("misbruik maken van")
accusation.append("illegale jacht op")
accusation.append("heling van")
accusation.append("auteursrechtenschending op")
accusation.append("schending van handelsembargo met betrekking tot")
accusation.append("handelen met voorkennis in")
accusation.append("illegale import van beschermde")
accusation.append("het plegen van economische delicten met behulp van")
accusation.append("discriminatie van")
accusation.append("het ontkennen van")
accusation.append("poging tot doodslag op")
accusation.append("valsmunterij met behulp van")
accusation.append("poging tot omkoperij van")
accusation.append("witwaspraktijken met")
accusation.append("het plegen van genocide op")

noun = []
noun.append("handgereedschappen")
noun.append("groenten")
noun.append("neutrino's")
noun.append("ledballonnen")
noun.append("bitcoins")
noun.append("precisiegereedschappen")
noun.append("relationele modellen")
noun.append("zwaartekracht")
noun.append("programmeerfouten")
noun.append("zwarte gaten")
noun.append("laserstralen")
noun.append("lolcats")
noun.append("SSL certificaten")
noun.append("supernova's")
noun.append("internet trolls")
noun.append("IPv6 pakketten")
noun.append("powertools")
noun.append("splijtstoffen")
noun.append("gramaticafouten") # Please do not correct misspelling :/)
noun.append("strijdgassen")
noun.append("deadlocks")
noun.append("toiletbrillen")
noun.append("onzinnige aangiftes")
noun.append("IRC bots")
noun.append("seksueel overdraagbare aandoeningen")
noun.append("geometrische vormen")
noun.append("priemgetallen")
noun.append("instant noodles")
noun.append("relativiteit")
noun.append("SCART stekkers")
noun.append("non-maskable interrupts")
noun.append("POSIX standaarden")
noun.append("ITIL procedures")
noun.append("  R O Z E    F * * * * * G    P O N I E S")
noun.append("museumstukken")

random_accusation = random.choice(accusation)
random_noun = random.choice(noun)

print 'Bij dezen wil ik aangifte tegen Hack42 doen wegens {} {}.'.format(random_accusation, random_noun)

