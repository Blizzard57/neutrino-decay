# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Sun 24 Oct 2021 15:40:07


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.n1,P.ve__tilde__):'((MH**2 - Mn1**2)*((ee**2*gN**2*MH**2*Mn1**2)/(4.*MW**2*sw**2) - (ee**2*gN**2*Mn1**4)/(4.*MW**2*sw**2)))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.n2,P.vm__tilde__):'((MH**2 - Mn2**2)*((ee**2*gN**2*MH**2*Mn2**2)/(4.*MW**2*sw**2) - (ee**2*gN**2*Mn2**4)/(4.*MW**2*sw**2)))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.n3,P.vt__tilde__):'((MH**2 - Mn3**2)*((ee**2*gN**2*MH**2*Mn3**2)/(4.*MW**2*sw**2) - (ee**2*gN**2*Mn3**4)/(4.*MW**2*sw**2)))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ve,P.n1):'((MH**2 - Mn1**2)*((ee**2*gN**2*MH**2*Mn1**2)/(4.*MW**2*sw**2) - (ee**2*gN**2*Mn1**4)/(4.*MW**2*sw**2)))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.vm,P.n2):'((MH**2 - Mn2**2)*((ee**2*gN**2*MH**2*Mn2**2)/(4.*MW**2*sw**2) - (ee**2*gN**2*Mn2**4)/(4.*MW**2*sw**2)))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.vt,P.n3):'((MH**2 - Mn3**2)*((ee**2*gN**2*MH**2*Mn3**2)/(4.*MW**2*sw**2) - (ee**2*gN**2*Mn3**4)/(4.*MW**2*sw**2)))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_n1 = Decay(name = 'Decay_n1',
                 particle = P.n1,
                 partial_widths = {(P.H,P.ve):'((-MH**2 + Mn1**2)*(-(ee**2*gN**2*MH**2*Mn1**2)/(4.*MW**2*sw**2) + (ee**2*gN**2*Mn1**4)/(4.*MW**2*sw**2)))/(32.*cmath.pi*abs(Mn1)**3)',
                                   (P.H,P.ve__tilde__):'((-MH**2 + Mn1**2)*(-(ee**2*gN**2*MH**2*Mn1**2)/(4.*MW**2*sw**2) + (ee**2*gN**2*Mn1**4)/(4.*MW**2*sw**2)))/(32.*cmath.pi*abs(Mn1)**3)',
                                   (P.W__plus__,P.e__minus__):'((Mn1**2 - MW**2)*((ee**2*gN**2*Mn1**2)/(2.*sw**2) + (ee**2*gN**2*Mn1**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Mn1)**3)',
                                   (P.W__minus__,P.e__plus__):'((Mn1**2 - MW**2)*((ee**2*gN**2*Mn1**2)/(2.*sw**2) + (ee**2*gN**2*Mn1**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Mn1)**3)',
                                   (P.Z,P.ve):'((Mn1**2 - MZ**2)*((ee**2*gN**2*Mn1**2)/(4.*cw**2*sw**2) + (ee**2*gN**2*Mn1**4)/(4.*cw**2*MZ**2*sw**2) - (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(32.*cmath.pi*abs(Mn1)**3)',
                                   (P.Z,P.ve__tilde__):'((Mn1**2 - MZ**2)*((ee**2*gN**2*Mn1**2)/(4.*cw**2*sw**2) + (ee**2*gN**2*Mn1**4)/(4.*cw**2*MZ**2*sw**2) - (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(32.*cmath.pi*abs(Mn1)**3)'})

Decay_n2 = Decay(name = 'Decay_n2',
                 particle = P.n2,
                 partial_widths = {(P.H,P.vm):'((-MH**2 + Mn2**2)*(-(ee**2*gN**2*MH**2*Mn2**2)/(4.*MW**2*sw**2) + (ee**2*gN**2*Mn2**4)/(4.*MW**2*sw**2)))/(32.*cmath.pi*abs(Mn2)**3)',
                                   (P.H,P.vm__tilde__):'((-MH**2 + Mn2**2)*(-(ee**2*gN**2*MH**2*Mn2**2)/(4.*MW**2*sw**2) + (ee**2*gN**2*Mn2**4)/(4.*MW**2*sw**2)))/(32.*cmath.pi*abs(Mn2)**3)',
                                   (P.W__plus__,P.mu__minus__):'((Mn2**2 - MW**2)*((ee**2*gN**2*Mn2**2)/(2.*sw**2) + (ee**2*gN**2*Mn2**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Mn2)**3)',
                                   (P.W__minus__,P.mu__plus__):'((Mn2**2 - MW**2)*((ee**2*gN**2*Mn2**2)/(2.*sw**2) + (ee**2*gN**2*Mn2**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Mn2)**3)',
                                   (P.Z,P.vm):'((Mn2**2 - MZ**2)*((ee**2*gN**2*Mn2**2)/(4.*cw**2*sw**2) + (ee**2*gN**2*Mn2**4)/(4.*cw**2*MZ**2*sw**2) - (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(32.*cmath.pi*abs(Mn2)**3)',
                                   (P.Z,P.vm__tilde__):'((Mn2**2 - MZ**2)*((ee**2*gN**2*Mn2**2)/(4.*cw**2*sw**2) + (ee**2*gN**2*Mn2**4)/(4.*cw**2*MZ**2*sw**2) - (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(32.*cmath.pi*abs(Mn2)**3)'})

Decay_n3 = Decay(name = 'Decay_n3',
                 particle = P.n3,
                 partial_widths = {(P.H,P.vt):'((-MH**2 + Mn3**2)*(-(ee**2*gN**2*MH**2*Mn3**2)/(4.*MW**2*sw**2) + (ee**2*gN**2*Mn3**4)/(4.*MW**2*sw**2)))/(32.*cmath.pi*abs(Mn3)**3)',
                                   (P.H,P.vt__tilde__):'((-MH**2 + Mn3**2)*(-(ee**2*gN**2*MH**2*Mn3**2)/(4.*MW**2*sw**2) + (ee**2*gN**2*Mn3**4)/(4.*MW**2*sw**2)))/(32.*cmath.pi*abs(Mn3)**3)',
                                   (P.W__plus__,P.ta__minus__):'(((ee**2*gN**2*Mn3**2)/(2.*sw**2) + (ee**2*gN**2*MTA**2)/(2.*sw**2) + (ee**2*gN**2*Mn3**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*Mn3**2*MTA**2)/(MW**2*sw**2) + (ee**2*gN**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*MW**2)/sw**2)*cmath.sqrt(Mn3**4 - 2*Mn3**2*MTA**2 + MTA**4 - 2*Mn3**2*MW**2 - 2*MTA**2*MW**2 + MW**4))/(32.*cmath.pi*abs(Mn3)**3)',
                                   (P.W__minus__,P.ta__plus__):'(((ee**2*gN**2*Mn3**2)/(2.*sw**2) + (ee**2*gN**2*MTA**2)/(2.*sw**2) + (ee**2*gN**2*Mn3**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*Mn3**2*MTA**2)/(MW**2*sw**2) + (ee**2*gN**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*MW**2)/sw**2)*cmath.sqrt(Mn3**4 - 2*Mn3**2*MTA**2 + MTA**4 - 2*Mn3**2*MW**2 - 2*MTA**2*MW**2 + MW**4))/(32.*cmath.pi*abs(Mn3)**3)',
                                   (P.Z,P.vt):'((Mn3**2 - MZ**2)*((ee**2*gN**2*Mn3**2)/(4.*cw**2*sw**2) + (ee**2*gN**2*Mn3**4)/(4.*cw**2*MZ**2*sw**2) - (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(32.*cmath.pi*abs(Mn3)**3)',
                                   (P.Z,P.vt__tilde__):'((Mn3**2 - MZ**2)*((ee**2*gN**2*Mn3**2)/(4.*cw**2*sw**2) + (ee**2*gN**2*Mn3**4)/(4.*cw**2*MZ**2*sw**2) - (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(32.*cmath.pi*abs(Mn3)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.n3):'(((ee**2*gN**2*Mn3**2)/(2.*sw**2) + (ee**2*gN**2*MTA**2)/(2.*sw**2) + (ee**2*gN**2*Mn3**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*Mn3**2*MTA**2)/(MW**2*sw**2) + (ee**2*gN**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*gN**2*MW**2)/sw**2)*cmath.sqrt(Mn3**4 - 2*Mn3**2*MTA**2 + MTA**4 - 2*Mn3**2*MW**2 - 2*MTA**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.n1,P.e__plus__):'((-Mn1**2 + MW**2)*(-(ee**2*gN**2*Mn1**2)/(2.*sw**2) - (ee**2*gN**2*Mn1**4)/(2.*MW**2*sw**2) + (ee**2*gN**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.n2,P.mu__plus__):'((-Mn2**2 + MW**2)*(-(ee**2*gN**2*Mn2**2)/(2.*sw**2) - (ee**2*gN**2*Mn2**4)/(2.*MW**2*sw**2) + (ee**2*gN**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.n3,P.ta__plus__):'((-(ee**2*gN**2*Mn3**2)/(2.*sw**2) - (ee**2*gN**2*MTA**2)/(2.*sw**2) - (ee**2*gN**2*Mn3**4)/(2.*MW**2*sw**2) + (ee**2*gN**2*Mn3**2*MTA**2)/(MW**2*sw**2) - (ee**2*gN**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*gN**2*MW**2)/sw**2)*cmath.sqrt(Mn3**4 - 2*Mn3**2*MTA**2 + MTA**4 - 2*Mn3**2*MW**2 - 2*MTA**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.n1,P.ve__tilde__):'((-Mn1**2 + MZ**2)*(-(ee**2*gN**2*Mn1**2)/(4.*cw**2*sw**2) - (ee**2*gN**2*Mn1**4)/(4.*cw**2*MZ**2*sw**2) + (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.n2,P.vm__tilde__):'((-Mn2**2 + MZ**2)*(-(ee**2*gN**2*Mn2**2)/(4.*cw**2*sw**2) - (ee**2*gN**2*Mn2**4)/(4.*cw**2*MZ**2*sw**2) + (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.n3,P.vt__tilde__):'((-Mn3**2 + MZ**2)*(-(ee**2*gN**2*Mn3**2)/(4.*cw**2*sw**2) - (ee**2*gN**2*Mn3**4)/(4.*cw**2*MZ**2*sw**2) + (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.n1):'((-Mn1**2 + MZ**2)*(-(ee**2*gN**2*Mn1**2)/(4.*cw**2*sw**2) - (ee**2*gN**2*Mn1**4)/(4.*cw**2*MZ**2*sw**2) + (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.n2):'((-Mn2**2 + MZ**2)*(-(ee**2*gN**2*Mn2**2)/(4.*cw**2*sw**2) - (ee**2*gN**2*Mn2**4)/(4.*cw**2*MZ**2*sw**2) + (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.n3):'((-Mn3**2 + MZ**2)*(-(ee**2*gN**2*Mn3**2)/(4.*cw**2*sw**2) - (ee**2*gN**2*Mn3**4)/(4.*cw**2*MZ**2*sw**2) + (ee**2*gN**2*MZ**2)/(2.*cw**2*sw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_zp = Decay(name = 'Decay_zp',
                 particle = P.zp,
                 partial_widths = {(P.b,P.b__tilde__):'(((32*gX**2*MB**2)/3. + (16*gX**2*Mzp**2)/3.)*cmath.sqrt(-4*MB**2*Mzp**2 + Mzp**4))/(48.*cmath.pi*abs(Mzp)**3)',
                                   (P.c,P.c__tilde__):'(gX**2*Mzp**4)/(9.*cmath.pi*abs(Mzp)**3)',
                                   (P.d,P.d__tilde__):'(gX**2*Mzp**4)/(9.*cmath.pi*abs(Mzp)**3)',
                                   (P.n1,P.n1):'((-64*gX**2*Mn1**2*zn1**2 + 16*gX**2*Mzp**2*zn1**2)*cmath.sqrt(-4*Mn1**2*Mzp**2 + Mzp**4))/(96.*cmath.pi*abs(Mzp)**3)',
                                   (P.n2,P.n2):'((-64*gX**2*Mn2**2*zn2**2 + 16*gX**2*Mzp**2*zn2**2)*cmath.sqrt(-4*Mn2**2*Mzp**2 + Mzp**4))/(96.*cmath.pi*abs(Mzp)**3)',
                                   (P.n3,P.n3):'((-64*gX**2*Mn3**2*zn3**2 + 16*gX**2*Mzp**2*zn3**2)*cmath.sqrt(-4*Mn3**2*Mzp**2 + Mzp**4))/(96.*cmath.pi*abs(Mzp)**3)',
                                   (P.s,P.s__tilde__):'(gX**2*Mzp**4)/(9.*cmath.pi*abs(Mzp)**3)',
                                   (P.t,P.t__tilde__):'(((32*gX**2*MT**2)/3. + (16*gX**2*Mzp**2)/3.)*cmath.sqrt(-4*MT**2*Mzp**2 + Mzp**4))/(48.*cmath.pi*abs(Mzp)**3)',
                                   (P.u,P.u__tilde__):'(gX**2*Mzp**4)/(9.*cmath.pi*abs(Mzp)**3)'})

