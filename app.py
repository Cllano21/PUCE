import pandas as pd
import dash
from dash import dcc, html, Input, Output, State
import os
from dash import callback_context  # Importar callback_context para manejar eventos
# Crear DataFrames con tus datos
datos_graduados = [
("2023", "Quito", "4014"),
("2023", "Ambato", "576"),
("2023", "Santo Domingo", "405"),
("2023", "Esmeraldas", "569"),
("2023", "Ibarra", "963"),
("2023", "Manabí", "924"),
("2023", "Nacional", "7451"),
("2022", "Quito", "3211"),
("2022", "Ambato", "542"),
("2022", "Santo Domingo", "421"),
("2022", "Esmeraldas", "502"),
("2022", "Ibarra", "763"),
("2022", "Manabí", "37"),
("2022", "Nacional", "5476"),
("2021", "Quito", "1840"),
("2021", "Ambato", "400"),
("2021", "Santo Domingo", "96"),
("2021", "Esmeraldas", "554"),
("2021", "Ibarra", "751"),
("2021", "Manabí", "NAN"),
("2021", "Nacional", "3641"),
]

datos_empleo = [
("2023", "Ambato", "Aún no consigo empleo desde mi graduación", "57"),
("2023", "Ambato", "Me tomó hasta 12 meses (un año) conseguir empleo", "31"),
("2023", "Ambato", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "8"),
("2023", "Ambato", "Me tomó hasta 24 meses (dos años) conseguir empleo", "3"),
("2023", "Ambato", "Me tomó hasta 6 meses conseguir empleo", "59"),
("2023", "Ambato", "Ya contaba con un empleo al momento de mi graduación", "164"),
("2023", "Esmeraldas", "Aún no consigo empleo desde mi graduación", "23"),
("2023", "Esmeraldas", "Me tomó hasta 12 meses (un año) conseguir empleo", "4"),
("2023", "Esmeraldas", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "2"),
("2023", "Esmeraldas", "Me tomó hasta 24 meses (dos años) conseguir empleo", "1"),
("2023", "Esmeraldas", "Me tomó hasta 6 meses conseguir empleo", "5"),
("2023", "Esmeraldas", "Ya contaba con un empleo al momento de mi graduación", "18"),
("2023", "Ibarra", "Aún no consigo empleo desde mi graduación", "53"),
("2023", "Ibarra", "Me tomó hasta 12 meses (un año) conseguir empleo", "26"),
("2023", "Ibarra", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "9"),
("2023", "Ibarra", "Me tomó hasta 24 meses (dos años) conseguir empleo", "1"),
("2023", "Ibarra", "Me tomó hasta 6 meses conseguir empleo", "41"),
("2023", "Ibarra", "Ya contaba con un empleo al momento de mi graduación", "95"),
("2023", "Quito", "Aún no consigo empleo desde mi graduación", "185"),
("2023", "Quito", "Me tomó hasta 12 meses (un año) conseguir empleo", "74"),
("2023", "Quito", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "21"),
("2023", "Quito", "Me tomó hasta 24 meses (dos años) conseguir empleo", "10"),
("2023", "Quito", "Me tomó hasta 6 meses conseguir empleo", "185"),
("2023", "Quito", "Ya contaba con un empleo al momento de mi graduación", "433"),
("2023", "Santo Domingo", "Aún no consigo empleo desde mi graduación", "29"),
("2023", "Santo Domingo", "Me tomó hasta 12 meses (un año) conseguir empleo", "7"),
("2023", "Santo Domingo", "Me tomó hasta 6 meses conseguir empleo", "15"),
("2023", "Santo Domingo", "Ya contaba con un empleo al momento de mi graduación", "22"),
("2023", "Manabí", "Aún no consigo empleo desde mi graduación", "38"),
("2023", "Manabí", "Me tomó hasta 12 meses (un año) conseguir empleo", "22"),
("2023", "Manabí", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "6"),
("2023", "Manabí", "Me tomó hasta 6 meses conseguir empleo", "36"),
("2023", "Manabí", "Ya contaba con un empleo al momento de mi graduación", "112"),
("2023", "Nacional", "Aún no consigo empleo desde mi graduación", "385"),
("2023", "Nacional", "Me tomó hasta 12 meses (un año) conseguir empleo", "164"),
("2023", "Nacional", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "46"),
("2023", "Nacional", "Me tomó hasta 24 meses (dos años) conseguir empleo", "15"),
("2023", "Nacional", "Me tomó hasta 6 meses conseguir empleo", "341"),
("2023", "Nacional", "Ya contaba con un empleo al momento de mi graduación", "844"),
("2022", "Ambato", "Aún no consigo empleo desde mi graduación", "31"),
("2022", "Ambato", "Me tomó hasta 12 meses (un año) conseguir empleo", "19"),
("2022", "Ambato", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "4"),
("2022", "Ambato", "Me tomó hasta 24 meses (dos años) conseguir empleo", "1"),
("2022", "Ambato", "Me tomó hasta 6 meses conseguir empleo", "34"),
("2022", "Ambato", "Ya contaba con un empleo al momento de mi graduación", "86"),
("2022", "Esmeraldas", "Aún no consigo empleo desde mi graduación", "52"),
("2022", "Esmeraldas", "Me tomó hasta 12 meses (un año) conseguir empleo", "8"),
("2022", "Esmeraldas", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "2"),
("2022", "Esmeraldas", "Me tomó hasta 24 meses (dos años) conseguir empleo", "3"),
("2022", "Esmeraldas", "Me tomó hasta 6 meses conseguir empleo", "9"),
("2022", "Esmeraldas", "Ya contaba con un empleo al momento de mi graduación", "39"),
("2022", "Ibarra", "Aún no consigo empleo desde mi graduación", "39"),
("2022", "Ibarra", "Me tomó hasta 12 meses (un año) conseguir empleo", "20"),
("2022", "Ibarra", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "7"),
("2022", "Ibarra", "Me tomó hasta 24 meses (dos años) conseguir empleo", "5"),
("2022", "Ibarra", "Me tomó hasta 6 meses conseguir empleo", "65"),
("2022", "Ibarra", "Ya contaba con un empleo al momento de mi graduación", "120"),
("2022", "Quito", "Aún no consigo empleo desde mi graduación", "165"),
("2022", "Quito", "Me tomó hasta 12 meses (un año) conseguir empleo", "89"),
("2022", "Quito", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "25"),
("2022", "Quito", "Me tomó hasta 24 meses (dos años) conseguir empleo", "15"),
("2022", "Quito", "Me tomó hasta 6 meses conseguir empleo", "233"),
("2022", "Quito", "Ya contaba con un empleo al momento de mi graduación", "362"),
("2022", "Santo Domingo", "Aún no consigo empleo desde mi graduación", "39"),
("2022", "Santo Domingo", "Me tomó hasta 12 meses (un año) conseguir empleo", "10"),
("2022", "Santo Domingo", "Me tomó hasta 24 meses (dos años) conseguir empleo", "1"),
("2022", "Santo Domingo", "Me tomó hasta 6 meses conseguir empleo", "35"),
("2022", "Santo Domingo", "Ya contaba con un empleo al momento de mi graduación", "53"),
("2022", "Manabí", "Aún no consigo empleo desde mi graduación", "6"),
("2022", "Manabí", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "1"),
("2022", "Manabí", "Me tomó hasta 6 meses conseguir empleo", "4"),
("2022", "Manabí", "Ya contaba con un empleo al momento de mi graduación", "5"),
("2022", "Nacional", "Aún no consigo empleo desde mi graduación", "332"),
("2022", "Nacional", "Me tomó hasta 12 meses (un año) conseguir empleo", "146"),
("2022", "Nacional", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "39"),
("2022", "Nacional", "Me tomó hasta 24 meses (dos años) conseguir empleo", "25"),
("2022", "Nacional", "Me tomó hasta 6 meses conseguir empleo", "380"),
("2022", "Nacional", "Ya contaba con un empleo al momento de mi graduación", "665"),
("2021", "Ambato", "Aún no consigo empleo desde mi graduación", "27"),
("2021", "Ambato", "Me tomó hasta 12 meses (un año) conseguir empleo", "23"),
("2021", "Ambato", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "4"),
("2021", "Ambato", "Me tomó hasta 24 meses (dos años) conseguir empleo", "3"),
("2021", "Ambato", "Me tomó hasta 6 meses conseguir empleo", "51"),
("2021", "Ambato", "Ya contaba con un empleo al momento de mi graduación", "132"),
("2021", "Esmeraldas", "Aún no consigo empleo desde mi graduación", "52"),
("2021", "Esmeraldas", "Me tomó hasta 12 meses (un año) conseguir empleo", "23"),
("2021", "Esmeraldas", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "5"),
("2021", "Esmeraldas", "Me tomó hasta 24 meses (dos años) conseguir empleo", "3"),
("2021", "Esmeraldas", "Me tomó hasta 6 meses conseguir empleo", "39"),
("2021", "Esmeraldas", "Ya contaba con un empleo al momento de mi graduación", "109"),
("2021", "Ibarra", "Aún no consigo empleo desde mi graduación", "30"),
("2021", "Ibarra", "Me tomó hasta 12 meses (un año) conseguir empleo", "10"),
("2021", "Ibarra", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "8"),
("2021", "Ibarra", "Me tomó hasta 24 meses (dos años) conseguir empleo", "3"),
("2021", "Ibarra", "Me tomó hasta 6 meses conseguir empleo", "42"),
("2021", "Ibarra", "Ya contaba con un empleo al momento de mi graduación", "154"),
("2021", "Quito", "Aún no consigo empleo desde mi graduación", "109"),
("2021", "Quito", "Me tomó hasta 12 meses (un año) conseguir empleo", "55"),
("2021", "Quito", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "8"),
("2021", "Quito", "Me tomó hasta 24 meses (dos años) conseguir empleo", "4"),
("2021", "Quito", "Me tomó hasta 6 meses conseguir empleo", "160"),
("2021", "Quito", "Ya contaba con un empleo al momento de mi graduación", "210"),
("2021", "Santo Domingo", "Aún no consigo empleo desde mi graduación", "10"),
("2021", "Santo Domingo", "Me tomó hasta 12 meses (un año) conseguir empleo", "5"),
("2021", "Santo Domingo", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "1"),
("2021", "Santo Domingo", "Me tomó hasta 6 meses conseguir empleo", "18"),
("2021", "Santo Domingo", "Ya contaba con un empleo al momento de mi graduación", "36"),
("2021", "Nacional", "Aún no consigo empleo desde mi graduación", "228"),
("2021", "Nacional", "Me tomó hasta 12 meses (un año) conseguir empleo", "116"),
("2021", "Nacional", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "26"),
("2021", "Nacional", "Me tomó hasta 24 meses (dos años) conseguir empleo", "13"),
("2021", "Nacional", "Me tomó hasta 6 meses conseguir empleo", "310"),
("2021", "Nacional", "Ya contaba con un empleo al momento de mi graduación", "641"),
]

datos_situacion = [
("2023", "Ambato", "Trabajando", "214"),
("2023", "Ambato", "Estudiando a tiempo completo por lo que no puedo trabajar", "17"),
("2023", "Ambato", "No estoy trabajando pero busco empleo", "51"),
("2023", "Ambato", "Soy emprendedor", "34"),
("2023", "Ambato", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "6"),
("2023", "Esmeraldas", "Trabajando", "25"),
("2023", "Esmeraldas", "Estudiando a tiempo completo por lo que no puedo trabajar", "2"),
("2023", "Esmeraldas", "No estoy trabajando pero busco empleo", "22"),
("2023", "Esmeraldas", "Soy emprendedor", "4"),
("2023", "Ibarra", "Trabajando", "125"),
("2023", "Ibarra", "Estudiando a tiempo completo por lo que no puedo trabajar", "1"),
("2023", "Ibarra", "No estoy trabajando pero busco empleo", "58"),
("2023", "Ibarra", "Soy emprendedor", "37"),
("2023", "Ibarra", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "4"),
("2023", "Quito", "Trabajando", "603"),
("2023", "Quito", "Estudiando a tiempo completo por lo que no puedo trabajar", "25"),
("2023", "Quito", "No estoy trabajando pero busco empleo", "203"),
("2023", "Quito", "Soy emprendedor", "59"),
("2023", "Quito", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "18"),
("2023", "Santo Domingo", "Trabajando", "35"),
("2023", "Santo Domingo", "No estoy trabajando pero busco empleo", "34"),
("2023", "Santo Domingo", "Soy emprendedor", "3"),
("2023", "Santo Domingo", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "1"),
("2023", "Manabí", "Trabajando", "142"),
("2023", "Manabí", "Estudiando a tiempo completo por lo que no puedo trabajar", "10"),
("2023", "Manabí", "No estoy trabajando pero busco empleo", "46"),
("2023", "Manabí", "Soy emprendedor", "16"),
("2023", "Nacional", "Trabajando", "1144"),
("2023", "Nacional", "Estudiando a tiempo completo por lo que no puedo trabajar", "55"),
("2023", "Nacional", "No estoy trabajando pero busco empleo", "414"),
("2023", "Nacional", "Soy emprendedor", "153"),
("2023", "Nacional", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "29"),
("2022", "Ambato", "Trabajando", "128"),
("2022", "Ambato", "No estoy trabajando", "43"),
("2022", "Ambato", "Estudiando a tiempo completo", "4"),
("2022", "Esmeraldas", "Trabajando", "50"),
("2022", "Esmeraldas", "No estoy trabajando", "62"),
("2022", "Esmeraldas", "Estudiando a tiempo completo", "1"),
("2022", "Ibarra", "Trabajando", "197"),
("2022", "Ibarra", "No estoy trabajando", "55"),
("2022", "Ibarra", "Estudiando a tiempo completo", "4"),
("2022", "Quito", "Trabajando", "631"),
("2022", "Quito", "No estoy trabajando", "236"),
("2022", "Quito", "Estudiando a tiempo completo", "22"),
("2022", "Santo Domingo", "Trabajando", "92"),
("2022", "Santo Domingo", "No estoy trabajando", "43"),
("2022", "Santo Domingo", "Estudiando a tiempo completo", "3"),
("2022", "Manabí", "Trabajando", "11"),
("2022", "Manabí", "No estoy trabajando", "5"),
("2022", "Nacional", "Trabajando", "1109"),
("2022", "Nacional", "No estoy trabajando", "444"),
("2022", "Nacional", "Estudiando a tiempo completo", "34"),
("2021", "Ambato", "No estoy trabajando pero busco empleo", "38"),
("2021", "Ambato", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "3"),
("2021", "Ambato", "Trabajando", "199"),
("2021", "Esmeraldas", "No estoy trabajando pero busco empleo", "75"),
("2021", "Esmeraldas", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "3"),
("2021", "Esmeraldas", "Trabajando", "153"),
("2021", "Ibarra", "No estoy trabajando pero busco empleo", "51"),
("2021", "Ibarra", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "5"),
("2021", "Ibarra", "Trabajando", "191"),
("2021", "Quito", "No estoy trabajando pero busco empleo", "173"),
("2021", "Quito", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "8"),
("2021", "Quito", "Trabajando", "365"),
("2021", "Santo Domingo", "No estoy trabajando pero busco empleo", "15"),
("2021", "Santo Domingo", "Trabajando", "55"),
("2021", "Nacional", "No estoy trabajando pero busco empleo", "352"),
("2021", "Nacional", "No estoy trabajando pero no tengo interés en buscar empleo actualmente", "19"),
("2021", "Nacional", "Trabajando", "963"),
]
datos_sector=[("2023", "Ambato", "No aplica", "108"),
("2023", "Ambato", "No aplica", "108"),
("2023", "Ambato", "Organización No Gubernamental /Organización de Sociedad Civil", "6"),
("2023", "Ambato", "Privado", "138"),
("2023", "Ambato", "Público", "70"),
("2023", "Esmeraldas", "No aplica", "28"),
("2023", "Esmeraldas", "Privado", "8"),
("2023", "Esmeraldas", "Público", "17"),
("2023", "Ibarra", "No aplica", "100"),
("2023", "Ibarra", "Organización No Gubernamental /Organización de Sociedad Civil", "1"),
("2023", "Ibarra", "Privado", "96"),
("2023", "Ibarra", "Público", "28"),
("2023", "Quito", "No aplica", "305"),
("2023", "Quito", "Organización No Gubernamental /Organización de Sociedad Civil", "16"),
("2023", "Quito", "Privado", "371"),
("2023", "Quito", "Público", "216"),
("2023", "Santo Domingo", "No aplica", "38"),
("2023", "Santo Domingo", "Organización No Gubernamental /Organización de Sociedad Civil", "2"),
("2023", "Santo Domingo", "Privado", "19"),
("2023", "Santo Domingo", "Público", "14"),
("2023", "Manabí", "No aplica", "72"),
("2023", "Manabí", "Organización No Gubernamental /Organización de Sociedad Civil", "4"),
("2023", "Manabí", "Privado", "76"),
("2023", "Manabí", "Público", "62"),
("2023", "Nacional", "No aplica", "651"),
("2023", "Nacional", "Organización No Gubernamental /Organización de Sociedad Civil", "29"),
("2023", "Nacional", "Privado", "708"),
("2023", "Nacional", "Público", "407"),
("2022", "Ambato", "No aplica", "47"),
("2022", "Ambato", "Organización No Gubernamental /Organización de Sociedad Civil", "1"),
("2022", "Ambato", "Privado", "76"),
("2022", "Ambato", "Público", "32"),
("2022", "Ambato", "Negocio propio / Emprendimiento / Independiente / Libre ejercicio", "19"),
("2022", "Esmeraldas", "No aplica", "63"),
("2022", "Esmeraldas", "Organización No Gubernamental /Organización de Sociedad Civil", "1"),
("2022", "Esmeraldas", "Privado", "20"),
("2022", "Esmeraldas", "Público", "23"),
("2022", "Esmeraldas", "Negocio propio / Emprendimiento / Independiente / Libre ejercicio", "6"),
("2022", "Ibarra", "No aplica", "59"),
("2022", "Ibarra", "Organización No Gubernamental /Organización de Sociedad Civil", "1"),
("2022", "Ibarra", "Privado", "94"),
("2022", "Ibarra", "Público", "49"),
("2022", "Ibarra", "Negocio propio / Emprendimiento / Independiente / Libre ejercicio", "53"),
("2022", "Quito", "No aplica", "258"),
("2022", "Quito", "Organización No Gubernamental /Organización de Sociedad Civil", "23"),
("2022", "Quito", "Privado", "408"),
("2022", "Quito", "Público", "149"),
("2022", "Quito", "Negocio propio / Emprendimiento / Independiente / Libre ejercicio", "51"),
("2022", "Santo Domingo", "No aplica", "46"),
("2022", "Santo Domingo", "Privado", "42"),
("2022", "Santo Domingo", "Público", "48"),
("2022", "Santo Domingo", "Negocio propio / Emprendimiento / Independiente / Libre ejercicio", "2"),
("2022", "Manabí", "No aplica", "5"),
("2022", "Manabí", "Privado", "8"),
("2022", "Manabí", "Público", "2"),
("2022", "Manabí", "Negocio propio / Emprendimiento / Independiente / Libre ejercicio", "1"),
("2022", "Nacional", "No aplica", "478"),
("2022", "Nacional", "Organización No Gubernamental /Organización de Sociedad Civil", "26"),
("2022", "Nacional", "Privado", "648"),
("2022", "Nacional", "Público", "303"),
("2022", "Nacional", "Negocio propio / Emprendimiento / Independiente / Libre ejercicio", "132"),
("2021", "Ambato", "Independiente / Libre ejercicio (ejercer la profesión de manera independiente y autónoma)", "15"),
("2021", "Ambato", "Negocio propio / Emprendimiento", "21"),
("2021", "Ambato", "No aplica", "41"),
("2021", "Ambato", "Organización No Gubernamental /Organización de Sociedad Civil", "6"),
("2021", "Ambato", "Privado", "76"),
("2021", "Ambato", "Público", "81"),
("2021", "Esmeraldas", "Independiente / Libre ejercicio (ejercer la profesión de manera independiente y autónoma)", "4"),
("2021", "Esmeraldas", "Negocio propio / Emprendimiento", "1"),
("2021", "Esmeraldas", "No aplica", "78"),
("2021", "Esmeraldas", "Privado", "48"),
("2021", "Esmeraldas", "Público", "100"),
("2021", "Ibarra", "Independiente / Libre ejercicio (ejercer la profesión de manera independiente y autónoma)", "50"),
("2021", "Ibarra", "Negocio propio / Emprendimiento", "15"),
("2021", "Ibarra", "No aplica", "56"),
("2021", "Ibarra", "Privado", "61"),
("2021", "Ibarra", "Público", "65"),
("2021", "Quito", "Independiente / Libre ejercicio (ejercer la profesión de manera independiente y autónoma)", "20"),
("2021", "Quito", "Negocio propio / Emprendimiento", "14"),
("2021", "Quito", "No aplica", "181"),
("2021", "Quito", "Organización No Gubernamental /Organización de Sociedad Civil", "12"),
("2021", "Quito", "Privado", "255"),
("2021", "Quito", "Público", "64"),
("2021", "Santo Domingo", "Independiente / Libre ejercicio (ejercer la profesión de manera independiente y autónoma)", "4"),
("2021", "Santo Domingo", "No aplica", "15"),
("2021", "Santo Domingo", "Privado", "28"),
("2021", "Santo Domingo", "Público", "23"),
("2021", "Nacional", "Independiente / Libre ejercicio (ejercer la profesión de manera independiente y autónoma)", "93"),
("2021", "Nacional", "Negocio propio / Emprendimiento", "51"),
("2021", "Nacional", "No aplica", "371"),
("2021", "Nacional", "Organización No Gubernamental /Organización de Sociedad Civil", "18"),
("2021", "Nacional", "Privado", "468"),
("2021", "Nacional", "Público", "333"),
]

datos_ocupacion=[
("2023", "Ambato", "Directivo/Gerencial", "19"),
("2023", "Ambato", "Mando Medio", "54"),
("2023", "Ambato", "No aplica", "108"),
("2023", "Ambato", "Operativo", "82"),
("2023", "Ambato", "Externo/consultor/servicios profesionales, etc", "48"),
("2023", "Ambato", "Propietario/Accionista", "11"),
("2023", "Esmeraldas", "Directivo/Gerencial", "2"),
("2023", "Esmeraldas", "Mando Medio", "8"),
("2023", "Esmeraldas", "No aplica", "28"),
("2023", "Esmeraldas", "Operativo", "12"),
("2023", "Esmeraldas", "Externo/consultor/servicios profesionales, etc", "3"),
("2023", "Ibarra", "Directivo/Gerencial", "18"),
("2023", "Ibarra", "Mando Medio", "27"),
("2023", "Ibarra", "No aplica", "100"),
("2023", "Ibarra", "Operativo", "47"),
("2023", "Ibarra", "Externo/consultor/servicios profesionales, etc", "22"),
("2023", "Ibarra", "Propietario/Accionista", "11"),
("2023", "Manabí", "Directivo/Gerencial", "18"),
("2023", "Manabí", "Mando Medio", "37"),
("2023", "Manabí", "No aplica", "72"),
("2023", "Manabí", "Operativo", "65"),
("2023", "Manabí", "Externo/consultor/servicios profesionales, etc", "20"),
("2023", "Manabí", "Propietario/Accionista", "2"),
("2023", "Quito", "Directivo/Gerencial", "49"),
("2023", "Quito", "Mando Medio", "175"),
("2023", "Quito", "No aplica", "305"),
("2023", "Quito", "Operativo", "296"),
("2023", "Quito", "Externo/consultor/servicios profesionales, etc", "73"),
("2023", "Quito", "Propietario/Accionista", "10"),
("2023", "Santo Domingo", "Directivo/Gerencial", "6"),
("2023", "Santo Domingo", "Mando Medio", "2"),
("2023", "Santo Domingo", "No aplica", "38"),
("2023", "Santo Domingo", "Operativo", "21"),
("2023", "Santo Domingo", "Externo/consultor/servicios profesionales, etc", "5"),
("2023", "Santo Domingo", "Propietario/Accionista", "1"),
("2023", "Nacional", "Directivo/Gerencial", "112"),
("2023", "Nacional", "Mando Medio", "303"),
("2023", "Nacional", "No aplica", "651"),
("2023", "Nacional", "Operativo", "523"),
("2023", "Nacional", "Externo/consultor/servicios profesionales, etc", "171"),
("2023", "Nacional", "Propietario/Accionista", "35"),
("2022", "Ambato", "Directivo/Gerencial", "14"),
("2022", "Ambato", "Mando Medio", "27"),
("2022", "Ambato", "No aplica", "47"),
("2022", "Ambato", "Operativo", "53"),
("2022", "Ambato", "Propietario", "11"),
("2022", "Ambato", "Externo/consultor/servicios profesionales, etc", "23"),
("2022", "Esmeraldas", "Directivo/Gerencial", "2"),
("2022", "Esmeraldas", "Mando Medio", "5"),
("2022", "Esmeraldas", "No aplica", "63"),
("2022", "Esmeraldas", "Operativo", "28"),
("2022", "Esmeraldas", "Propietario", "6"),
("2022", "Esmeraldas", "Externo/consultor/servicios profesionales, etc", "9"),
("2022", "Ibarra", "Directivo/Gerencial", "16"),
("2022", "Ibarra", "Mando Medio", "35"),
("2022", "Ibarra", "No aplica", "59"),
("2022", "Ibarra", "Operativo", "59"),
("2022", "Ibarra", "Propietario", "62"),
("2022", "Ibarra", "Externo/consultor/servicios profesionales, etc", "25"),
("2022", "Manabí", "Mando Medio", "3"),
("2022", "Manabí", "No aplica", "5"),
("2022", "Manabí", "Operativo", "5"),
("2022", "Manabí", "Externo/consultor/servicios profesionales, etc", "3"),
("2022", "Quito", "Directivo/Gerencial", "39"),
("2022", "Quito", "Mando Medio", "100"),
("2022", "Quito", "No aplica", "258"),
("2022", "Quito", "Operativo", "327"),
("2022", "Quito", "Propietario", "55"),
("2022", "Quito", "Externo/consultor/servicios profesionales, etc", "110"),
("2022", "Santo Domingo", "Directivo/Gerencial", "7"),
("2022", "Santo Domingo", "Mando Medio", "8"),
("2022", "Santo Domingo", "No aplica", "46"),
("2022", "Santo Domingo", "Operativo", "59"),
("2022", "Santo Domingo", "Propietario", "2"),
("2022", "Santo Domingo", "Externo/consultor/servicios profesionales, etc", "16"),
("2022", "Nacional", "Directivo/Gerencial", "78"),
("2022", "Nacional", "Mando Medio", "178"),
("2022", "Nacional", "No aplica", "478"),
("2022", "Nacional", "Operativo", "531"),
("2022", "Nacional", "Propietario", "136"),
("2022", "Nacional", "Externo/consultor/servicios profesionales, etc", "186"),
("2021", "Ambato", "Directivo/Gerencial", "21"),
("2021", "Ambato", "Externo (consultor)", "4"),
("2021", "Ambato", "Mando Medio", "35"),
("2021", "Ambato", "No aplica", "56"),
("2021", "Ambato", "Operativo", "52"),
("2021", "Ambato", "Otros:", "50"),
("2021", "Ambato", "Propietario", "22"),
("2021", "Esmeraldas", "Directivo/Gerencial", "8"),
("2021", "Esmeraldas", "Externo (consultor)", "1"),
("2021", "Esmeraldas", "Mando Medio", "26"),
("2021", "Esmeraldas", "No aplica", "82"),
("2021", "Esmeraldas", "Operativo", "70"),
("2021", "Esmeraldas", "Otros:", "42"),
("2021", "Esmeraldas", "Propietario", "2"),
("2021", "Ibarra", "Directivo/Gerencial", "14"),
("2021", "Ibarra", "Mando Medio", "35"),
("2021", "Ibarra", "No aplica", "106"),
("2021", "Ibarra", "Operativo", "52"),
("2021", "Ibarra", "Otros:", "24"),
("2021", "Ibarra", "Propietario", "16"),
("2021", "Quito", "Directivo/Gerencial", "17"),
("2021", "Quito", "Externo (consultor)", "9"),
("2021", "Quito", "Mando Medio", "84"),
("2021", "Quito", "No aplica", "201"),
("2021", "Quito", "Operativo", "186"),
("2021", "Quito", "Otros:", "37"),
("2021", "Quito", "Propietario", "12"),
("2021", "Santo Domingo", "Directivo/Gerencial", "4"),
("2021", "Santo Domingo", "Externo (consultor)", "1"),
("2021", "Santo Domingo", "Mando Medio", "9"),
("2021", "Santo Domingo", "No aplica", "19"),
("2021", "Santo Domingo", "Operativo", "22"),
("2021", "Santo Domingo", "Otros:", "14"),
("2021", "Santo Domingo", "Propietario", "1"),
("2021", "Nacional", "Directivo/Gerencial", "64"),
("2021", "Nacional", "Externo (consultor)", "15"),
("2021", "Nacional", "Mando Medio", "189"),
("2021", "Nacional", "No aplica", "464"),
("2021", "Nacional", "Operativo", "382"),
("2021", "Nacional", "Otros:", "167"),
("2021", "Nacional", "Propietario", "53"),
]
# [TODOS LOS DATOS PERMANECEN IGUALES HASTA EL FINAL DE datos_sector]
# Crear DataFrames con la columna de año
df_graduados = pd.DataFrame(datos_graduados, columns=["Año", "SEDES", "Graduados"])
df_empleo = pd.DataFrame(datos_empleo, columns=["Año", "SEDES", "Conseguir empleo", "Participantes"])
df_situacion = pd.DataFrame(datos_situacion, columns=["Año", "SEDES", "Situación laboral", "Participantes"])
df_sector = pd.DataFrame(datos_sector, columns=["Año", "SEDES", "Sector", "Participantes"])  # Nuevo DataFrame
df_ocupacion = pd.DataFrame(datos_ocupacion, columns=["Año", "SEDES", "Ocupación", "Participantes"])
df_ocupacion["Participantes"] = pd.to_numeric(df_ocupacion["Participantes"], errors="coerce")
# Convertir a numérico
df_graduados["Graduados"] = pd.to_numeric(df_graduados["Graduados"], errors="coerce")
df_empleo["Participantes"] = pd.to_numeric(df_empleo["Participantes"], errors="coerce")
df_situacion["Participantes"] = pd.to_numeric(df_situacion["Participantes"], errors="coerce")
df_sector["Participantes"] = pd.to_numeric(df_sector["Participantes"], errors="coerce")  # Nuevo
# Crear DataFrames (los datos permanecen iguales)
# ... [LOS DATOS PERMANECEN IGUALES HASTA EL FINAL DE df_sector] ...



# Crear DataFrames (los datos permanecen iguales)
# ... [LOS DATOS PERMANECEN IGUALES HASTA EL FINAL DE df_sector] ...

# Obtener listas únicas para los dropdowns
años_disponibles = sorted(df_graduados["Año"].unique().tolist())
sedes_disponibles = sorted([s for s in df_empleo["SEDES"].unique().tolist()], key=lambda x: x.lower())

# App
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(style={
    "fontFamily": "Arial, sans-serif",
    "padding": "20px",
    "maxWidth": "1400px",
    "margin": "0 auto",
    "backgroundColor": "#f8f9fa"
}, children=[
    # Título
    html.H1("Análisis de Graduados y Empleo", style={
        "textAlign": "center",
        "color": "#1e3a8a",
        "marginBottom": "30px"
    }),
    
    # Controles de filtro
    html.Div(style={
        "display": "flex",
        "flexWrap": "wrap",
        "gap": "20px",
        "marginBottom": "30px",
        "alignItems": "flex-end"
    }, children=[
        # Dropdown para seleccionar año
        html.Div(style={"flex": "1", "minWidth": "200px"}, children=[
            html.Label("Seleccionar Año:", style={"fontWeight": "bold", "marginBottom": "5px"}),
            dcc.Dropdown(
                id="selector-anio",
                options=[{"label": año, "value": año} for año in años_disponibles] + 
                        [{"label": "Todos los años", "value": "Todos"}],
                value=años_disponibles[0] if años_disponibles else None,
                clearable=False
            )
        ]),
        
        # Dropdown para seleccionar sede (ahora incluye Nacional)
        html.Div(style={"flex": "2", "minWidth": "250px"}, children=[
            html.Label("Seleccionar Sede:", style={"fontWeight": "bold", "marginBottom": "5px"}),
            dcc.Dropdown(
                id="selector-sedes",
                options=[{"label": sede, "value": sede} for sede in sedes_disponibles],
                value=sedes_disponibles[0] if sedes_disponibles else None,
                clearable=False
            )
        ]),
        
        # Botón para mostrar todos los años
        html.Div(style={"flex": "1", "minWidth": "150px"}, children=[
            html.Label("Acción rápida:", style={"fontWeight": "bold", "marginBottom": "5px"}),
            html.Button(
                "Todos los años",
                id="boton-todos-anios",
                n_clicks=0,
                style={
                    "width": "100%",
                    "padding": "10px",
                    "backgroundColor": "#1e3a8a",
                    "color": "white",
                    "border": "none",
                    "borderRadius": "4px",
                    "cursor": "pointer",
                    "fontWeight": "bold"
                }
            )
        ])
    ]),
    
    # Tarjeta para mostrar el número de graduados
    html.Div(id="graduados-numero", style={
        "padding": "20px",
        "backgroundColor": "white",
        "borderRadius": "8px",
        "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
        "marginBottom": "30px",
        "textAlign": "center"
    }),
    
    # Contenedor para las tres tablas
    html.Div(style={
        "display": "flex",
        "gap": "15px",
        "marginBottom": "30px",
        "flexWrap": "wrap"
    }, children=[
        # Tabla de empleo
        html.Div(style={"flex": "1", "minWidth": "350px"}, children=[
            html.H2("Tiempo para Conseguir Empleo", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-empleo")
        ]),
        
        # Tabla de situación laboral
        html.Div(style={"flex": "1", "minWidth": "350px"}, children=[
            html.H2("Situación Laboral Actual", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-situacion")
        ]),
        
        # Tabla de sector laboral
        html.Div(style={"flex": "1", "minWidth": "350px"}, children=[
            html.H2("Sector Laboral", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-sector")
        ]),
                html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Ocupación Laboral", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-ocupacion")
    ])
])
])

# Callback para manejar el botón "Todos los años"
@app.callback(
    Output("selector-anio", "value"),
    Input("boton-todos-anios", "n_clicks"),
    prevent_initial_call=True
)
def manejar_boton_todos_anios(n_clicks):
    return "Todos"

# Callback para actualizar el número de graduados
@app.callback(
    Output("graduados-numero", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_numero_graduados(anio_seleccionado, sede_seleccionada):
    # Filtrar por sede
    df_filtrado = df_graduados[df_graduados["SEDES"] == sede_seleccionada]
    
    # Manejar caso de "Todos los años"
    if anio_seleccionado == "Todos":
        resultado = df_filtrado["Graduados"].sum()
        return html.Div([
            html.H3(f"Sede: {sede_seleccionada} (Todos los años)"),
            html.P(f"Total de graduados: {int(resultado):,}", style={
                "fontSize": "32px",
                "color": "#1e3a8a",
                "fontWeight": "bold",
                "margin": "10px 0"
            }),
            html.Small("Datos acumulados de todos los años", style={"color": "#4b5563"})
        ])
    
    # Filtrar por año específico
    df_filtrado = df_filtrado[df_filtrado["Año"] == anio_seleccionado]
    
    # Obtener el resultado
    if not df_filtrado.empty:
        resultado = df_filtrado["Graduados"].iloc[0]
    else:
        resultado = None
    
    # Formatear el resultado
    if resultado is None or pd.isna(resultado):
        return html.Div([
            html.H3(f"Sede: {sede_seleccionada} ({anio_seleccionado})"),
            html.P("No hay datos disponibles de graduados", style={
                "fontSize": "24px",
                "color": "#dc2626",
                "fontWeight": "bold"
            })
        ])
    else:
        return html.Div([
            html.H3(f"Sede: {sede_seleccionada} ({anio_seleccionado})"),
            html.P(f"Total de graduados: {int(resultado):,}", style={
                "fontSize": "32px",
                "color": "#1e3a8a",
                "fontWeight": "bold",
                "margin": "10px 0"
            }),
            html.Small("Datos de graduados disponibles", style={"color": "#4b5563"})
        ])

# Función para crear tabla con datos de múltiples años
def crear_tabla_con_multianios(df, categoria_col, participantes_col, anio_seleccionado, sede_seleccionada):
    # Filtrar por sede
    df_filtrado = df[df["SEDES"] == sede_seleccionada]
    
    # Manejar caso de "Todos los años"
    if anio_seleccionado == "Todos":
        # Agrupar por año y categoría
        df_agrupado = df_filtrado.groupby(["Año", categoria_col])[participantes_col].sum().reset_index()
        
        # Pivotar para tener años como columnas
        df_pivot = df_agrupado.pivot(index=categoria_col, columns="Año", values=participantes_col).reset_index()
        df_pivot = df_pivot.fillna(0)
        
        # Calcular totales
        años_cols = [str(a) for a in años_disponibles]
        df_pivot["Total"] = df_pivot[años_cols].sum(axis=1)
        total_general = df_pivot["Total"].sum()
        
        # Calcular porcentajes
        if total_general > 0:
            df_pivot["% Total"] = (df_pivot["Total"] / total_general * 100).round(1)
        else:
            df_pivot["% Total"] = 0.0
        
        # Crear encabezado
        encabezado = [html.Th(categoria_col, style={"padding": "10px 15px", "textAlign": "left", "fontSize": "14px"})]
        for año in años_disponibles:
            encabezado.append(html.Th(año, style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"}))
        encabezado.append(html.Th("Total", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"}))
        encabezado.append(html.Th("%", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"}))
        encabezado = [html.Tr(encabezado)]
        
        # Crear filas de datos
        filas = []
        for _, row in df_pivot.iterrows():
            celda_categoria = html.Td(row[categoria_col], style={"padding": "10px 15px", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"})
            celdas_anios = []
            for año in años_disponibles:
                valor = int(row[str(año)]) if str(año) in df_pivot.columns else 0
                celdas_anios.append(html.Td(f"{valor:,}", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}))
            
            celda_total = html.Td(f"{int(row['Total']):,}", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"})
            celda_porcentaje = html.Td(f"{row['% Total']:.1f}%", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"})
            
            filas.append(html.Tr([celda_categoria] + celdas_anios + [celda_total, celda_porcentaje]))
        
        # Crear tabla completa
        return html.Table(
            encabezado + filas,
            style={
                "width": "100%",
                "borderCollapse": "collapse",
                "backgroundColor": "white",
                "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
                "borderRadius": "8px",
                "overflow": "hidden"
            }
        )
    
    # Caso para un solo año
    df_filtrado = df_filtrado[df_filtrado["Año"] == anio_seleccionado]
    
    if df_filtrado.empty:
        return html.Div(f"No hay datos disponibles para {sede_seleccionada} en {anio_seleccionado}", style={
            "textAlign": "center",
            "padding": "20px",
            "color": "#dc2626"
        })
    
    # Calcular porcentajes
    total_participantes = df_filtrado[participantes_col].sum()
    if total_participantes > 0:
        df_filtrado["Porcentaje"] = (df_filtrado[participantes_col] / total_participantes * 100).round(1)
    else:
        df_filtrado["Porcentaje"] = 0.0
    
    # Crear tabla simple
    encabezado = html.Tr([
        html.Th(categoria_col, style={"padding": "10px 15px", "textAlign": "left", "fontSize": "14px"}),
        html.Th("Participantes", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"}),
        html.Th("Porcentaje", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"})
    ])
    
    filas = []
    for _, row in df_filtrado.iterrows():
        filas.append(html.Tr([
            html.Td(row[categoria_col], style={"padding": "10px 15px", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}),
            html.Td(f"{int(row[participantes_col]):,}", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}),
            html.Td(f"{row['Porcentaje']:.1f}%", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"})
        ]))
    
    return html.Table(
        [encabezado] + filas,
        style={
            "width": "100%",
            "borderCollapse": "collapse",
            "backgroundColor": "white",
            "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
            "borderRadius": "8px",
            "overflow": "hidden"
        }
    )

# Callbacks para actualizar las tablas
@app.callback(
    Output("tabla-empleo", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_tabla_empleo(anio_seleccionado, sede_seleccionada):
    return crear_tabla_con_multianios(
        df_empleo, 
        "Conseguir empleo", 
        "Participantes",
        anio_seleccionado, 
        sede_seleccionada
    )

@app.callback(
    Output("tabla-situacion", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_tabla_situacion(anio_seleccionado, sede_seleccionada):
    return crear_tabla_con_multianios(
        df_situacion, 
        "Situación laboral", 
        "Participantes",
        anio_seleccionado, 
        sede_seleccionada
    )

@app.callback(
    Output("tabla-sector", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_tabla_sector(anio_seleccionado, sede_seleccionada):
    return crear_tabla_con_multianios(
        df_sector, 
        "Sector", 
        "Participantes",
        anio_seleccionado, 
        sede_seleccionada
    )
@app.callback(
    Output("tabla-ocupacion", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_tabla_ocupacion(anio_seleccionado, sede_seleccionada):
    return crear_tabla_con_multianios(
        df_ocupacion, 
        "Ocupación", 
        "Participantes",
        anio_seleccionado, 
        sede_seleccionada
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run(host='0.0.0.0', port=port, debug=True)