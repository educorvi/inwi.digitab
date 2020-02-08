# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

dokumentarten = SimpleVocabulary(
    [
        SimpleTerm(value=u'unfallanzeige', token=u'unfallanzeige', title=u'Unfallanzeige'),
        SimpleTerm(value=u'd-arzt-bericht', token=u'd-arzt-bericht', title=u'D-Arzt-Bericht'),
        SimpleTerm(value=u'h-arzt-bericht', token=u'h-arzt-bericht', title=u'H-Arzt-Bericht'),
        SimpleTerm(value=u'e-rechnung', token=u'e-rechnung', title=u'E-Rechnung'),
   ]) 

dale = SimpleVocabulary(
    [
        SimpleTerm(value=u'heute', token=u'heute', title=u'heute'),
        SimpleTerm(value=u'vin_1', token=u'vin_1', title=u'[vin_1] Nachname d. Versicherten'),
        SimpleTerm(value=u'vin_2', token=u'vin_2', title=u'[vin_2] Vorname d. Versicherten'),
        SimpleTerm(value=u'vin_3', token=u'vin_3', title=u'[vin_3] StA. Versicherter'),
        SimpleTerm(value=u'vin_4', token=u'vin_4', title=u'[vin_4] Geschlecht d. Versicherten'),
        SimpleTerm(value=u'vin_5', token=u'vin_5', title=u'[vin_5] PLZ d. Versicherten '),
        SimpleTerm(value=u'vin_6', token=u'vin_6', title=u'[vin_6] Ort des Versicherten'),
        SimpleTerm(value=u'vin_7', token=u'vin_7', title=u'[vin_7] Str/Hnr. des Versicherten'),
        SimpleTerm(value=u'vin_8', token=u'vin_8', title=u'[vin_8] Lkz des Wohnortes'),
        SimpleTerm(value=u'vin_9', token=u'vin_9', title=u'[vin_9] Geb.datum des Versicherten'),
        SimpleTerm(value=u'vin_10',token=u'vin_10',title=u'[vin_10] Telefon des Versicherten'),
        SimpleTerm(value=u'vin_11',token=u'vin_11',title=u'[vin_11] Versichertennummer GKV'),
        SimpleTerm(value=u'eti_1', token=u'eti_1', title=u'[eti_1] Eingetroffen am'),
        SimpleTerm(value=u'eti_2', token=u'eti_2', title=u'[eti_2] Eintreffzeit'),
        SimpleTerm(value=u'unb_4', token=u'unb_4', title=u'[unb_4] Erstellungsdatum LE'),
        SimpleTerm(value=u'unb_5', token=u'unb_5', title=u'[unb_5] Uhrzeit der Erstellung'),
        SimpleTerm(value=u'uvt_1', token=u'uvt_1', title=u'[uvt_1] Name UVT'),
        SimpleTerm(value=u'uvt_2', token=u'uvt_2', title=u'[uvt_2] IK Nummer UVT'),
        SimpleTerm(value=u'uvt_3', token=u'uvt_3', title=u'[uvt_3] Erstellungsdatum Bericht'),
        SimpleTerm(value=u'uvt_4', token=u'uvt_4', title=u'[uvt_4] Unfalltag'),
        SimpleTerm(value=u'uvt_5', token=u'uvt_5', title=u'[uvt_5] Aktenzeichen des UVT'),
        SimpleTerm(value=u'ufb_1', token=u'ufb_1', title=u'[ufb_1] Firmenname'),
        SimpleTerm(value=u'ufb_2', token=u'ufb_2', title=u'[ufb_2] Lkz des Unfallbetriebes'),
        SimpleTerm(value=u'ufb_3', token=u'ufb_3', title=u'[ufb_3] PLZ des Unfallbetriebes'),
        SimpleTerm(value=u'ufb_4', token=u'ufb_4', title=u'[ufb_4] Ort des Unfallbetriebes'),
        SimpleTerm(value=u'ufb_5', token=u'ufb_5', title=u'[ufb_5] Str/Hnr. Unfallbetrieb'),
        SimpleTerm(value=u'ufb_6', token=u'ufb_6', title=u'[ufb_6] Beschäftigt als'),
        SimpleTerm(value=u'ufb_7', token=u'ufb_7', title=u'[ufb_7] Beschäftigt seit'),
        SimpleTerm(value=u'ksd_1', token=u'ksd_1', title=u'[ksd_1] Krankenkasse Name'),
        SimpleTerm(value=u'ksd_5', token=u'ksd_5', title=u'[ksd_5] Familienversicherung'),
        SimpleTerm(value=u'ksd_2', token=u'ksd_2', title=u'[ksd_2] Krankenkasse IKNr. GKV'),
        SimpleTerm(value=u'ksd_3', token=u'ksd_3', title=u'[ksd_3] Pflegekasse Name'),
        SimpleTerm(value=u'ksd_4', token=u'ksd_4', title=u'[ksd_4] Pflegekasse IK-Nr.'),
        SimpleTerm(value=u'ufd_1', token=u'ufd_1', title=u'[ufd_1] Unfallzeit'),
        SimpleTerm(value=u'ufd_2', token=u'ufd_2', title=u'[ufd_2] Arbeitszeit Beginn'),
        SimpleTerm(value=u'ufd_3', token=u'ufd_3', title=u'[ufd_3] Arbeitszeit Ende'),
        SimpleTerm(value=u'ebh_1', token=u'ebh_1', title=u'[ebh_1] Erstbehandlung ab'),
        SimpleTerm(value=u'ebh_2', token=u'ebh_2', title=u'[ebh_2] Erstbehandlung Arzt'),
        SimpleTerm(value=u'bef_1', token=u'bef_1', title=u'[bef_1] Blutentnahme ja/nein'),
        SimpleTerm(value=u'bef_2', token=u'bef_2', title=u'[bef_2] Alkohol, Drogen, Med.'),
        SimpleTerm(value=u'bef_3', token=u'bef_3', title=u'[bef_3] Anzeichen Sucht-/BTM'),
        SimpleTerm(value=u'dis_1', token=u'dis_1', title=u'[dis_1] Diagnosetext'),
        SimpleTerm(value=u'dis_4', token=u'dis_4', title=u'[dis_4] Diagnoseschlüssel'),
        SimpleTerm(value=u'dis_3', token=u'dis_3', title=u'[dis_3] Diagnosecode'),
        SimpleTerm(value=u'tdh_1', token=u'tdh_1', title=u'[tdh_1] Unfallhergang'),
        SimpleTerm(value=u'tdh_2', token=u'tdh_2', title=u'[tdh_2] Unfallverhalten'),
        SimpleTerm(value=u'tdh_3', token=u'tdh_3', title=u'[tdh_3] Befund'),
        SimpleTerm(value=u'tdh_4', token=u'tdh_4', title=u'[tdh_4] Röntgenergebnis'),
        SimpleTerm(value=u'tdh_5', token=u'tdh_5', title=u'[tdh_5] Art der Erstversorgung'),
        SimpleTerm(value=u'tdh_6', token=u'tdh_6', title=u'[tdh_6] Erstversorgung nicht D-Arzt'),
        SimpleTerm(value=u'tdh_7', token=u'tdh_7', title=u'[tdh_7] Unfallabh. Beeinträchtigungen'),
        SimpleTerm(value=u'bed_1', token=u'bed_1', title=u'[bed_1] Annahme kein Arbeitsunfall'),
        SimpleTerm(value=u'bed_2', token=u'bed_2', title=u'[bed_2] Bedenken zu Arbeitsunfall'),
        SimpleTerm(value=u'beh_1', token=u'beh_1', title=u'[beh_1] Art der Behandlung'),
        SimpleTerm(value=u'beh_15',token=u'beh_15',title=u'[beh_15] keine Behandlung, weil:'),
        SimpleTerm(value=u'beh_2', token=u'beh_2', title=u'[beh_2] Behandlungstyp'),
        SimpleTerm(value=u'beh_3', token=u'beh_3', title=u'[beh_3] Behandlung durch'),
        SimpleTerm(value=u'beh_4', token=u'beh_4', title=u'[beh_4] Verletzung nach VAV'),
        SimpleTerm(value=u'beh_5', token=u'beh_5', title=u'[beh_5] Ziffer des VAV-Kataloges'),
        SimpleTerm(value=u'beh_6', token=u'beh_6', title=u'[beh_6] Nachschau am: (Datum)'),
        SimpleTerm(value=u'beh_7', token=u'beh_7', title=u'[beh_7] Weiterb. Praxis/KKH '),
        SimpleTerm(value=u'beh_8', token=u'beh_8', title=u'[beh_8] Praxis/KKH Str/Hnr'),
        SimpleTerm(value=u'beh_9', token=u'beh_9', title=u'[beh_9] Praxis/KKH PLZ'),
        SimpleTerm(value=u'beh_10',token=u'beh_10',title=u'[beh_10] Praxis/KKH Ort'),
        SimpleTerm(value=u'beh_11',token=u'beh_11',title=u'[beh_11] Praxis/KKH LKZ'),
        SimpleTerm(value=u'beh_14',token=u'beh_14',title=u'[beh_14] Weiterl. an Arzt/KKH'),
        SimpleTerm(value=u'afb_1', token=u'afb_1', title=u'[afb_1] Arbeitsfähig'),
        SimpleTerm(value=u'afb_4', token=u'afb_4', title=u'[afb_4] Arbeitunfähig ab'),
        SimpleTerm(value=u'afb_7', token=u'afb_7', title=u'[afb_7] vrs. arbeitsfähig ab'),
        SimpleTerm(value=u'afb_8', token=u'afb_8', title=u'[afb_8] vrs. Dauer über 6 Monate'),
        SimpleTerm(value=u'ber_1', token=u'ber_1', title=u'[ber_1] Beratung durch UVT'),
        SimpleTerm(value=u'ber_2', token=u'ber_2', title=u'[ber_2] Beratung weil:'),
        SimpleTerm(value=u'kon_1', token=u'kon_1', title=u'[kon_1] Konsiliararzt ja/nein'),
        SimpleTerm(value=u'kon_2', token=u'kon_2', title=u'[kon_2] Name des Konsiliararztes'),
        SimpleTerm(value=u'kon_3', token=u'kon_3', title=u'[kon_3] Str/Hnr. d. Konsiliararztes'),
        SimpleTerm(value=u'kon_4', token=u'kon_4', title=u'[kon_4] PLZ des Konsiliararztes'),
        SimpleTerm(value=u'kon_5', token=u'kon_5', title=u'[kon_5] Ort des Konsiliararztes'),
        SimpleTerm(value=u'kon_6', token=u'kon_6', title=u'[kon_6] LKZ des Konsiliararztes'),
        SimpleTerm(value=u'kon_7', token=u'kon_7', title=u'[kon_7] Weiterl. an Konsiliararzt'),
        SimpleTerm(value=u'sri_1', token=u'sri_1', title=u'[sri_1] Art der Heilbehandlung'),
        SimpleTerm(value=u'sri_2', token=u'sri_2', title=u'[sri_2] Rechnungstyp'),
        SimpleTerm(value=u'sri_3', token=u'sri_3', title=u'[sri_3] Ost-Abschlag'),
        SimpleTerm(value=u'sri_4', token=u'sri_4', title=u'[sri_4] Summe Gebühr'),
        SimpleTerm(value=u'sri_5', token=u'sri_5', title=u'[sri_5] Summe Besondere Kosten'),
        SimpleTerm(value=u'sri_6', token=u'sri_6', title=u'[sri_6] Summe Allgemeine Kosten'),
        SimpleTerm(value=u'sri_7', token=u'sri_7', title=u'[sri_7] Summe Sachkosten'),
        SimpleTerm(value=u'rel_1', token=u'rel_1', title=u'[rel_1] Leistungsdatum'),
        SimpleTerm(value=u'rel_2', token=u'rel_2', title=u'[rel_2] Gebühr'),
        SimpleTerm(value=u'rel_3', token=u'rel_3', title=u'[rel_3] Leistungsposition'),
        SimpleTerm(value=u'rel_4', token=u'rel_4', title=u'[rel_4] Leistungsposition Schlüssel'),
        SimpleTerm(value=u'rel_5', token=u'rel_5', title=u'[rel_5] Besondere Kosten'),
        SimpleTerm(value=u'rel_6', token=u'rel_6', title=u'[rel_6] Allgemeine Kosten'),
        SimpleTerm(value=u'rel_7', token=u'rel_7', title=u'[rel_7] Sachkosten Kosten'),
        SimpleTerm(value=u'rel_8', token=u'rel_8', title=u'[rel_8] Bemerkungen'),
        SimpleTerm(value=u'kto_1', token=u'kto_1', title=u'[kto_1] Gesamtbetrag'),
        SimpleTerm(value=u'kto_2', token=u'kto_2', title=u'[kto_2] Rechnungsnummer'),
        SimpleTerm(value=u'kto_3', token=u'kto_3', title=u'[kto_3] IK des Zahlungsempfängers'),
        SimpleTerm(value=u'abs_1', token=u'abs_1', title=u'[abs_1] Absendername'),
        SimpleTerm(value=u'abs_2', token=u'abs_2', title=u'[abs_2] Str./Hnr. des Absenders'),
        SimpleTerm(value=u'abs_3', token=u'abs_3', title=u'[abs_3] PLZ des Absenders'),
        SimpleTerm(value=u'abs_4', token=u'abs_4', title=u'[abs_4] Ort des Absenders'),
        SimpleTerm(value=u'abs_5', token=u'abs_5', title=u'[abs_5] LKZ des Absenders'),
        SimpleTerm(value=u'abs_6', token=u'abs_6', title=u'[abs_6] Telefon des Absenders'),
        SimpleTerm(value=u'abs_7', token=u'abs_7', title=u'[abs_7] Ansp. des Absenders'),
        SimpleTerm(value=u'not_1', token=u'not_1', title=u'[not_1] Notiz'),
        SimpleTerm(value=u'swh_1', token=u'swh_1', title=u'[swh_1] Softwarename'),
        SimpleTerm(value=u'swh_2', token=u'swh_2', title=u'[swh_2] Name des SW-Moduls'),
        SimpleTerm(value=u'swi_1', token=u'swi_1', title=u'[swi_1] Felderkennung'),
        SimpleTerm(value=u'swi_2', token=u'swi_2', title=u'[swi_2] Feldinhalt')
        ])
