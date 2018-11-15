#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Simulation de circuits logiques """


class Fil:
    """ Relie les composants et déclenche leur actualisation """

    def __init__(self):
        self.composants_aval = []
        self.etat = False

    def ajouter_composant_aval(self, composant):
        """ Ajoute un composant que le fil peut activer """
        self.composants_aval.append(composant)

    def set_etat(self, etat):
        """ Actualise les composants en aval """
        self.etat = etat
        for composant in self.composants_aval:
            composant.update()


class Porte:
    """ Porte logique munie de deux entrées et d'une sortie """

    def __init__(self, entree_un, entree_deux, sortie):
        self.entrees = [entree_un, entree_deux]
        self.sortie = sortie

    def fonction(self):
        return False

    def update(self):
        self.sortie.set_etat(self.fonction())


class PorteAND(Porte):
    """ Porte réalisant l'opération logique 'et' """

    def fonction(self):
        return self.entrees[0].etat and self.entrees[1].etat


class PorteOR(Porte):
    """ Porte réalisant l'opération logique 'ou' """

    def fonction(self):
        return self.entrees[0].etat or self.entrees[1].etat


class PorteXOR(Porte):
    """ Porte réalisant l'opération logique 'ou exclusif' """

    def fonction(self):
        return self.entrees[0].etat or self.entrees[1].etat and not (
            self.entrees[0].etat and self.entrees[1].etat)


class PorteNOT(Porte):
    """ Porte niant son entrée """

    def __init__(self, entree, sortie):
        self.entree = entree
        self.sortie = sortie

    def fonction(self):
        return not (self.entree)


class Sensor:
    """ Capteur """

    def __init__(self, entree):
        self.entree = entree

    def update(self):
        print(self.entree.etat)


class DemiAdd:
    """ Demi-additionneur """

    def __init__(self, entree_un, entree_deux, sortie_un, sortie_deux):
        self.entrees = [entree_un, entree_deux]
        self.sorties = [sortie_un, sortie_deux]

    def update(self):
        e1, e2 = self.sorties[0].etat, self.sorties[0].etat
        self.sorties[0].set_etat(e1 and e2)
        self.sorties[1].set_etat(e1 or e2 and not (e1 and e2))


class Add:
    """ Additionneur pourvu de deux demi-additionneurs """

    def __init__(self, entree_un, entree_deux, retenue, sortie_un,
                 sortie_deux):
        c, d, e = Fil(), Fil(), Fil()

        self.sorties = [sortie_un, sortie_deux]
        self.demi_add1 = DemiAdd(entree_un, entree_deux, c, d)
        self.demi_add2 = DemiAdd(c, retenue, sortie_un, e)
        self.porte_or = PorteOR(d, e, sortie_deux)

        c.ajouter_composant_aval(self.demi_add2)
        e.ajouter_composant_aval(self.porte_or)
        d.ajouter_composant_aval(self.porte_or)

    def update(self):
        return None


def test_base():
    """ Circuit logique d'exemple """
    a, b, c, d = Fil(), Fil(), Fil(), Fil()
    porte1 = PorteNOT(a, b)
    porte2 = PorteOR(b, c, d)
    sensor = Sensor(d)

    a.ajouter_composant_aval(porte1)
    b.ajouter_composant_aval(porte2)
    c.ajouter_composant_aval(porte2)

    d.ajouter_composant_aval(sensor)

    c.set_etat(False)
    a.set_etat(True)
    c.set_etat(True)
    a.set_etat(False)


def test_demi_add():
    """ Table de vérité du demi-additionneur """
    a, b, c, d = Fil(), Fil(), Fil(), Fil()
    sensor1, sensor2 = Sensor(c), Sensor(d)
    demi_add = DemiAdd(a, b, c, d)

    a.ajouter_composant_aval(demi_add)
    b.ajouter_composant_aval(demi_add)

    c.ajouter_composant_aval(sensor1)
    d.ajouter_composant_aval(sensor2)
    for e1 in [True, False]:
        for e2 in [True, False]:
            a.set_etat(e1)
            b.set_etat(e2)


def test_add():
    """ Table de vérité de l'additionneur """
    a, b, c, d, r = Fil(), Fil(), Fil(), Fil(), Fil()
    sensor1, sensor2 = Sensor(c), Sensor(d)
    additionneur = Add(a, b, r, c, d)

    a.ajouter_composant_aval(additionneur)
    b.ajouter_composant_aval(additionneur)
    r.ajouter_composant_aval(additionneur)

    c.ajouter_composant_aval(sensor1)
    d.ajouter_composant_aval(sensor2)

    for e1 in [True, False]:
        for e2 in [True, False]:
            for e3 in [True, False]:
                a.set_etat(e1)
                b.set_etat(e2)
                r.set_etat(e3)


if __name__ == "__main__":
    test_base()
    test_demi_add()
    test_add()
