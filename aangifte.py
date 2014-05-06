#!/bin/python
"""
##############################################################################
#
#          FILE: aangifte.py
#
#         USAGE: ./aangifte.py
#   DESCRIPTION: Prints a possible reason to accuse someone based on a
#                random crime (accusation) and a random noun, with often
#                hilarious results.
#                I'm in the process of learning Python, so this is probably
#                quite ugly.
#       OPTIONS: None
#  REQUIREMENTS: python, random
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Dennis van Zuijlekom, <dvanzuijlekom@hack42.nl>
#       COMPANY: Hackerspace Hack42 Arnhem
#       VERSION: 1.3
#       CREATED: 2014-04-15
#      MODIFIED: Tue 06 May 2014 22:13:42 CEST
#      REVISION: ---
##############################################################################
#       CHANGES: 2014-04-15, DVZ, 1.0
#                Initial release.
#                2014-04-22, DVZ, 1.1
#                Added a few accusations and nouns
#                2014-05-03, DVZ, 1.2
#                Some more accusations and nouns, sorted lists
#                2014-05-06, DVZ, 1.3
#                Moar!
##############################################################################
"""

import random

accusation = []
accusation.append("auteursrechtenschending op")
accusation.append("belediging van")
accusation.append("discriminatie van")
accusation.append("bedreiging met")
accusation.append("handelen met voorkennis in")
accusation.append("heling van")
accusation.append("het beramen van een terroristische aanslag met")
accusation.append("het illegaal dumpen van")
accusation.append("het in een openbare ruimte onder invloed zijn van")
accusation.append("het in diskrediet brengen van")
accusation.append("het inwendig smokkelen van")
accusation.append("het kapen van")
accusation.append("het mishandelen van")
accusation.append("het na 22:00 's avonds geluidsoverlast veroorzaken met")
accusation.append("het negeren van bord C.21, verbod op")
accusation.append("het ontkennen van")
accusation.append("het plegen van economische delicten met behulp van")
accusation.append("het plegen van genocide op")
accusation.append("het plegen van oorlogshandelingen met")
accusation.append("het slaktofferen van")
accusation.append("het zonder vergunning bedienen van")
accusation.append("huisvredebreuk met")
accusation.append("illegale import van beschermde")
accusation.append("illegale jacht op")
accusation.append("misbruik maken van")
accusation.append("obscene gedragingen met")
accusation.append("onrechtmatig gebruik van")
accusation.append("openbare schennispleging met")
accusation.append("overtreding van IETF RFC 1855 met betrekking tot")
accusation.append("poging tot doodslag op")
accusation.append("poging tot omkoperij van")
accusation.append("schending van handelsembargo met betrekking tot")
accusation.append("valsheid in geschrifte met behulp van")
accusation.append("valsmunterij met behulp van")
accusation.append("verboden bezit van")
accusation.append("verduisteren van")
accusation.append("vernieling van")
accusation.append("verstoring van de openbare orde, gebruikmakend van")
accusation.append("vervalsing van")
accusation.append("witwaspraktijken met")

noun = []
noun.append("  R O Z E    F * * * * * G    P O N I E S")
noun.append("1024 bit RSA keys")
noun.append("IPv6 pakketten")
noun.append("IRC bots")
noun.append("ITIL procedures")
noun.append("MediaWiki forms")
noun.append("POSIX standaarden")
noun.append("SCART stekkers")
noun.append("SSL certificaten")
noun.append("WHOIS data")
noun.append("afgeschreven hardware")
noun.append("beamers")
noun.append("besturingssystemen")
noun.append("bitcoins")
noun.append("broedplaatsen")
noun.append("de interwebs")
noun.append("deadlocks")
noun.append("email-zeep")
noun.append("free energy")
noun.append("geometrische vormen")
noun.append("gramaticafouten") # Please do not correct misspelling :/)
noun.append("groenten")
noun.append("handgereedschappen")
noun.append("Happy End toiletpapier")
noun.append("hyperlinks")
noun.append("instant noodles")
noun.append("internet trolls")
noun.append("Japanese technology")
noun.append("kwantummechanica")
noun.append("laserstralen")
noun.append("ledballonnen")
noun.append("lolcats")
noun.append("motorkettingzagen")
noun.append("museumstukken")
noun.append("neutrino's")
noun.append("niet-gecertificeerde software")
noun.append("non-maskable interrupts")
noun.append("onzinnige aangiftes")
noun.append("powertools")
noun.append("precisiegereedschappen")
noun.append("priemgetallen")
noun.append("programmeerfouten")
noun.append("relationele modellen")
noun.append("relativiteit")
noun.append("rottende sojabonen")
noun.append("seksueel overdraagbare aandoeningen")
noun.append("splijtstoffen")
noun.append("strijdgassen")
noun.append("supernova's")
noun.append("toiletbrillen")
noun.append("typemachines")
noun.append("zeeglas")
noun.append("zwaartekracht")
noun.append("zwarte gaten")

random_accusation = random.choice(accusation)
random_noun = random.choice(noun)

print 'Bij dezen wil ik aangifte tegen Hack42 doen wegens {} {}.'.format(random_accusation, random_noun)

