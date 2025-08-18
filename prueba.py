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
datos_nivelsalario=[
("2023", "Ambato", "No aplica", "108"),
("2023", "Ambato", "No contesta", "11"),
("2023", "Ambato", "Entre uno y tres salarios básicos", "127"),
("2023", "Ambato", "Un salario básico o menos", "28"),
("2023", "Ambato", "Entre cinco y siete salarios básicos", "6"),
("2023", "Ambato", "Entre tres y cinco salarios básicos", "29"),
("2023", "Ambato", "Más de nueve salarios básicos", "1"),
("2023", "Ambato", "Menor a 1 salario básico", "12"),
("2023", "Esmeraldas", "No aplica", "28"),
("2023", "Esmeraldas", "No contesta", "3"),
("2023", "Esmeraldas", "Entre uno y tres salarios básicos", "17"),
("2023", "Esmeraldas", "Entre cinco y siete salarios básicos", "1"),
("2023", "Esmeraldas", "Entre tres y cinco salarios básicos", "1"),
("2023", "Esmeraldas", "Menor a 1 salario básico", "3"),
("2023", "Ibarra", "No aplica", "100"),
("2023", "Ibarra", "No contesta", "4"),
("2023", "Ibarra", "Entre uno y tres salarios básicos", "80"),
("2023", "Ibarra", "Un salario básico o menos", "14"),
("2023", "Ibarra", "Entre cinco y siete salarios básicos", "4"),
("2023", "Ibarra", "Entre tres y cinco salarios básicos", "9"),
("2023", "Ibarra", "Menor a 1 salario básico", "13"),
("2023", "Ibarra", "Entre siete y nueve salarios básicos", "1"),
("2023", "Quito", "No aplica", "305"),
("2023", "Quito", "No contesta", "30"),
("2023", "Quito", "Entre uno y tres salarios básicos", "337"),
("2023", "Quito", "Un salario básico o menos", "39"),
("2023", "Quito", "Entre cinco y siete salarios básicos", "49"),
("2023", "Quito", "Entre tres y cinco salarios básicos", "113"),
("2023", "Quito", "Más de nueve salarios básicos", "8"),
("2023", "Quito", "Menor a 1 salario básico", "18"),
("2023", "Quito", "Entre siete y nueve salarios básicos", "9"),
("2023", "Santo Domingo", "No aplica", "38"),
("2023", "Santo Domingo", "No contesta", "1"),
("2023", "Santo Domingo", "Entre uno y tres salarios básicos", "17"),
("2023", "Santo Domingo", "Un salario básico o menos", "4"),
("2023", "Santo Domingo", "Entre cinco y siete salarios básicos", "2"),
("2023", "Santo Domingo", "Entre tres y cinco salarios básicos", "6"),
("2023", "Santo Domingo", "Menor a 1 salario básico", "5"),
("2023", "Manabí", "No aplica", "72"),
("2023", "Manabí", "No contesta", "9"),
("2023", "Manabí", "Entre uno y tres salarios básicos", "76"),
("2023", "Manabí", "Un salario básico o menos", "14"),
("2023", "Manabí", "Entre cinco y siete salarios básicos", "5"),
("2023", "Manabí", "Entre tres y cinco salarios básicos", "32"),
("2023", "Manabí", "Más de nueve salarios básicos", "1"),
("2023", "Manabí", "Menor a 1 salario básico", "4"),
("2023", "Manabí", "Entre siete y nueve salarios básicos", "1"),
("2023", "Nacional", "No aplica", "651"),
("2023", "Nacional", "No contesta", "58"),
("2023", "Nacional", "Entre uno y tres salarios básicos", "654"),
("2023", "Nacional", "Un salario básico o menos", "99"),
("2023", "Nacional", "Entre cinco y siete salarios básicos", "67"),
("2023", "Nacional", "Entre tres y cinco salarios básicos", "190"),
("2023", "Nacional", "Más de nueve salarios básicos", "10"),
("2023", "Nacional", "Menor a 1 salario básico", "55"),
("2023", "Nacional", "Entre siete y nueve salarios básicos", "11"),
("2022", "Ambato", "No aplica", "47"),
("2022", "Ambato", "No contesta", "4"),
("2022", "Ambato", "Entre uno y tres salarios básicos", "83"),
("2022", "Ambato", "Un salario básico o menos", "26"),
("2022", "Ambato", "Entre tres y cinco salarios básicos", "11"),
("2022", "Ambato", "Más de nueve salarios básicos", "2"),
("2022", "Ambato", "Entre cinco y siete salarios básicos", "1"),
("2022", "Ambato", "Entre siete y nueve salarios básicos", "1"),
("2022", "Esmeraldas", "No aplica", "63"),
("2022", "Esmeraldas", "No contesta", "4"),
("2022", "Esmeraldas", "Entre uno y tres salarios básicos", "32"),
("2022", "Esmeraldas", "Un salario básico o menos", "11"),
("2022", "Esmeraldas", "Entre tres y cinco salarios básicos", "2"),
("2022", "Esmeraldas", "Más de nueve salarios básicos", "1"),
("2022", "Ibarra", "No aplica", "59"),
("2022", "Ibarra", "No contesta", "13"),
("2022", "Ibarra", "Entre uno y tres salarios básicos", "101"),
("2022", "Ibarra", "Un salario básico o menos", "60"),
("2022", "Ibarra", "Entre tres y cinco salarios básicos", "17"),
("2022", "Ibarra", "Entre cinco y siete salarios básicos", "5"),
("2022", "Ibarra", "Entre siete y nueve salarios básicos", "1"),
("2022", "Quito", "No aplica", "258"),
("2022", "Quito", "No contesta", "29"),
("2022", "Quito", "Entre uno y tres salarios básicos", "321"),
("2022", "Quito", "Un salario básico o menos", "101"),
("2022", "Quito", "Entre tres y cinco salarios básicos", "86"),
("2022", "Quito", "Más de nueve salarios básicos", "13"),
("2022", "Quito", "Entre cinco y siete salarios básicos", "73"),
("2022", "Quito", "Entre siete y nueve salarios básicos", "8"),
("2022", "Santo Domingo", "No aplica", "46"),
("2022", "Santo Domingo", "No contesta", "5"),
("2022", "Santo Domingo", "Entre uno y tres salarios básicos", "64"),
("2022", "Santo Domingo", "Un salario básico o menos", "19"),
("2022", "Santo Domingo", "Entre tres y cinco salarios básicos", "3"),
("2022", "Santo Domingo", "Entre siete y nueve salarios básicos", "1"),
("2022", "Manabí", "No aplica", "5"),
("2022", "Manabí", "Entre uno y tres salarios básicos", "6"),
("2022", "Manabí", "Un salario básico o menos", "3"),
("2022", "Manabí", "Entre tres y cinco salarios básicos", "2"),
("2022", "Nacional", "No aplica", "478"),
("2022", "Nacional", "No contesta", "55"),
("2022", "Nacional", "Entre uno y tres salarios básicos", "607"),
("2022", "Nacional", "Un salario básico o menos", "220"),
("2022", "Nacional", "Entre tres y cinco salarios básicos", "121"),
("2022", "Nacional", "Más de nueve salarios básicos", "16"),
("2022", "Nacional", "Entre cinco y siete salarios básicos", "79"),
("2022", "Nacional", "Entre siete y nueve salarios básicos", "11"),
("2021", "Ambato", "Un salario básico o menos", "25"),
("2021", "Ambato", "Entre cinco y siete salarios básicos", "5"),
("2021", "Ambato", "Entre tres y cinco salarios básicos", "31"),
("2021", "Ambato", "Entre uno y tres salarios básicos", "130"),
("2021", "Ambato", "Más de nueve salarios básicos", "1"),
("2021", "Ambato", "No aplica", "41"),
("2021", "Ambato", "No contesta", "7"),
("2021", "Esmeraldas", "Un salario básico o menos", "14"),
("2021", "Esmeraldas", "Entre cinco y siete salarios básicos", "1"),
("2021", "Esmeraldas", "Entre tres y cinco salarios básicos", "16"),
("2021", "Esmeraldas", "Entre uno y tres salarios básicos", "112"),
("2021", "Esmeraldas", "No aplica", "78"),
("2021", "Esmeraldas", "No contesta", "10"),
("2021", "Ibarra", "Un salario básico o menos", "35"),
("2021", "Ibarra", "Entre cinco y siete salarios básicos", "6"),
("2021", "Ibarra", "Entre siete y nueve salarios básicos", "1"),
("2021", "Ibarra", "Entre tres y cinco salarios básicos", "26"),
("2021", "Ibarra", "Entre uno y tres salarios básicos", "115"),
("2021", "Ibarra", "Más de nueve salarios básicos", "1"),
("2021", "Ibarra", "No aplica", "56"),
("2021", "Ibarra", "No contesta", "7"),
("2021", "Quito", "Un salario básico o menos", "44"),
("2021", "Quito", "Entre cinco y siete salarios básicos", "17"),
("2021", "Quito", "Entre siete y nueve salarios básicos", "2"),
("2021", "Quito", "Entre tres y cinco salarios básicos", "56"),
("2021", "Quito", "Entre uno y tres salarios básicos", "229"),
("2021", "Quito", "Más de nueve salarios básicos", "1"),
("2021", "Quito", "No aplica", "181"),
("2021", "Quito", "No contesta", "16"),
("2021", "Santo Domingo", "Un salario básico o menos", "11"),
("2021", "Santo Domingo", "Entre cinco y siete salarios básicos", "1"),
("2021", "Santo Domingo", "Entre tres y cinco salarios básicos", "3"),
("2021", "Santo Domingo", "Entre uno y tres salarios básicos", "36"),
("2021", "Santo Domingo", "Más de nueve salarios básicos", "1"),
("2021", "Santo Domingo", "No aplica", "15"),
("2021", "Santo Domingo", "No contesta", "3"),
("2021", "Nacional", "Un salario básico o menos", "129"),
("2021", "Nacional", "Entre cinco y siete salarios básicos", "30"),
("2021", "Nacional", "Entre siete y nueve salarios básicos", "3"),
("2021", "Nacional", "Entre tres y cinco salarios básicos", "132"),
("2021", "Nacional", "Entre uno y tres salarios básicos", "622"),
("2021", "Nacional", "Más de nueve salarios básicos", "4"),
("2021", "Nacional", "No aplica", "371"),
("2021", "Nacional", "No contesta", "43"),
]
datos_relacion=[
("2023", "Ambato", "1", "13"),
("2023", "Ambato", "2", "15"),
("2023", "Ambato", "3", "42"),
("2023", "Ambato", "4", "66"),
("2023", "Ambato", "5", "78"),
("2023", "Ambato", "No aplica", "108"),
("2023", "Esmeraldas", "2", "1"),
("2023", "Esmeraldas", "4", "10"),
("2023", "Esmeraldas", "5", "14"),
("2023", "Esmeraldas", "No aplica", "28"),
("2023", "Ibarra", "1", "8"),
("2023", "Ibarra", "2", "2"),
("2023", "Ibarra", "3", "22"),
("2023", "Ibarra", "4", "48"),
("2023", "Ibarra", "5", "45"),
("2023", "Ibarra", "No aplica", "100"),
("2023", "Quito", "1", "22"),
("2023", "Quito", "2", "51"),
("2023", "Quito", "3", "120"),
("2023", "Quito", "4", "205"),
("2023", "Quito", "5", "205"),
("2023", "Quito", "No aplica", "305"),
("2023", "Santo Domingo", "2", "2"),
("2023", "Santo Domingo", "3", "6"),
("2023", "Santo Domingo", "4", "15"),
("2023", "Santo Domingo", "5", "12"),
("2023", "Santo Domingo", "No aplica", "38"),
("2023", "Manabí", "1", "14"),
("2023", "Manabí", "2", "2"),
("2023", "Manabí", "3", "23"),
("2023", "Manabí", "4", "31"),
("2023", "Manabí", "5", "72"),
("2023", "Manabí", "No aplica", "72"),
("2023", "Nacional", "1", "57"),
("2023", "Nacional", "2", "73"),
("2023", "Nacional", "3", "213"),
("2023", "Nacional", "4", "375"),
("2023", "Nacional", "5", "426"),
("2023", "Nacional", "No aplica", "651"),
("2022", "Ambato", "1", "7"),
("2022", "Ambato", "2", "5"),
("2022", "Ambato", "3", "32"),
("2022", "Ambato", "4", "33"),
("2022", "Ambato", "5", "51"),
("2022", "Ambato", "No aplica", "47"),
("2022", "Esmeraldas", "1", "2"),
("2022", "Esmeraldas", "2", "5"),
("2022", "Esmeraldas", "3", "6"),
("2022", "Esmeraldas", "4", "9"),
("2022", "Esmeraldas", "5", "28"),
("2022", "Esmeraldas", "No aplica", "63"),
("2022", "Ibarra", "1", "8"),
("2022", "Ibarra", "2", "8"),
("2022", "Ibarra", "3", "35"),
("2022", "Ibarra", "4", "56"),
("2022", "Ibarra", "5", "90"),
("2022", "Ibarra", "No aplica", "59"),
("2022", "Quito", "1", "28"),
("2022", "Quito", "2", "47"),
("2022", "Quito", "3", "136"),
("2022", "Quito", "4", "181"),
("2022", "Quito", "5", "239"),
("2022", "Quito", "No aplica", "258"),
("2022", "Santo Domingo", "1", "6"),
("2022", "Santo Domingo", "2", "5"),
("2022", "Santo Domingo", "3", "18"),
("2022", "Santo Domingo", "4", "26"),
("2022", "Santo Domingo", "5", "37"),
("2022", "Santo Domingo", "No aplica", "46"),
("2022", "Manabí", "1", "2"),
("2022", "Manabí", "2", "2"),
("2022", "Manabí", "3", "1"),
("2022", "Manabí", "4", "2"),
("2022", "Manabí", "5", "4"),
("2022", "Manabí", "No aplica", "5"),
("2022", "Nacional", "1", "53"),
("2022", "Nacional", "2", "72"),
("2022", "Nacional", "3", "228"),
("2022", "Nacional", "4", "307"),
("2022", "Nacional", "5", "449"),
("2022", "Nacional", "No aplica", "478"),
("2021", "Ambato", "1", "9"),
("2021", "Ambato", "2", "13"),
("2021", "Ambato", "3", "44"),
("2021", "Ambato", "4", "63"),
("2021", "Ambato", "5", "70"),
("2021", "Ambato", "(en blanco)", "41"),
("2021", "Esmeraldas", "1", "7"),
("2021", "Esmeraldas", "2", "3"),
("2021", "Esmeraldas", "3", "19"),
("2021", "Esmeraldas", "4", "44"),
("2021", "Esmeraldas", "5", "80"),
("2021", "Esmeraldas", "(en blanco)", "78"),
("2021", "Ibarra", "1", "13"),
("2021", "Ibarra", "2", "6"),
("2021", "Ibarra", "3", "35"),
("2021", "Ibarra", "4", "53"),
("2021", "Ibarra", "5", "84"),
("2021", "Ibarra", "(en blanco)", "56"),
("2021", "Quito", "1", "22"),
("2021", "Quito", "2", "25"),
("2021", "Quito", "3", "80"),
("2021", "Quito", "4", "110"),
("2021", "Quito", "5", "128"),
("2021", "Quito", "(en blanco)", "181"),
("2021", "Santo Domingo", "1", "3"),
("2021", "Santo Domingo", "2", "2"),
("2021", "Santo Domingo", "3", "10"),
("2021", "Santo Domingo", "4", "20"),
("2021", "Santo Domingo", "5", "20"),
("2021", "Santo Domingo", "(en blanco)", "15"),
("2021", "Nacional", "1", "54"),
("2021", "Nacional", "2", "49"),
("2021", "Nacional", "3", "188"),
("2021", "Nacional", "4", "290"),
("2021", "Nacional", "5", "382"),
("2021", "Nacional", "(en blanco)", "371"),
]
datos_nivelalcanzado=[
("2023", "Ambato", "Posgrado", "36"),
("2023", "Ambato", "No poseo títulos adicionales al de la PUCE", "181"),
("2023", "Ambato", "Grado", "100"),
("2023", "Ambato", "Doctorado/PhD", "1"),
("2023", "Ambato", "Tecnología", "4"),
("2023", "Esmeraldas", "Posgrado", "4"),
("2023", "Esmeraldas", "No poseo títulos adicionales al de la PUCE", "34"),
("2023", "Esmeraldas", "Grado", "12"),
("2023", "Esmeraldas", "Tecnología", "3"),
("2023", "Ibarra", "Posgrado", "18"),
("2023", "Ibarra", "No poseo títulos adicionales al de la PUCE", "174"),
("2023", "Ibarra", "Grado", "22"),
("2023", "Ibarra", "Tecnología", "11"),
("2023", "Quito", "Posgrado", "117"),
("2023", "Quito", "No poseo títulos adicionales al de la PUCE", "521"),
("2023", "Quito", "Grado", "244"),
("2023", "Quito", "Doctorado/PhD", "3"),
("2023", "Quito", "Tecnología", "23"),
("2023", "Santo Domingo", "Posgrado", "10"),
("2023", "Santo Domingo", "No poseo títulos adicionales al de la PUCE", "47"),
("2023", "Santo Domingo", "Grado", "16"),
("2023", "Manabí", "Posgrado", "35"),
("2023", "Manabí", "No poseo títulos adicionales al de la PUCE", "88"),
("2023", "Manabí", "Grado", "87"),
("2023", "Manabí", "Doctorado/PhD", "1"),
("2023", "Manabí", "Tecnología", "3"),
("2023", "Nacional", "Posgrado", "220"),
("2023", "Nacional", "No poseo títulos adicionales al de la PUCE", "1045"),
("2023", "Nacional", "Grado", "481"),
("2023", "Nacional", "Doctorado/PhD", "5"),
("2023", "Nacional", "Tecnología", "44"),
("2022", "Ambato", "Grado", "7"),
("2022", "Ambato", "Grado", "112"),
("2022", "Ambato", "Posgrado", "56"),
("2022", "Esmeraldas", "Doctorado/PhD", "1"),
("2022", "Esmeraldas", "Grado", "90"),
("2022", "Esmeraldas", "Posgrado", "22"),
("2022", "Ibarra", "Grado", "172"),
("2022", "Ibarra", "Posgrado", "84"),
("2022", "Quito", "Grado", "26"),
("2022", "Quito", "Doctorado/PhD", "3"),
("2022", "Quito", "Grado", "630"),
("2022", "Quito", "Posgrado", "230"),
("2022", "Santo Domingo", "Grado", "84"),
("2022", "Santo Domingo", "Posgrado", "54"),
("2022", "Manabí", "Grado", "15"),
("2022", "Manabí", "Posgrado", "1"),
("2022", "Nacional", "Grado", "33"),
("2022", "Nacional", "Doctorado/PhD", "4"),
("2022", "Nacional", "Grado", "1103"),
("2022", "Nacional", "Posgrado", "447"),
("2021", "Ambato", "Grado", "4"),
("2021", "Ambato", "Grado", "102"),
("2021", "Ambato", "Posgrado", "134"),
("2021", "Esmeraldas", "Grado", "2"),
("2021", "Esmeraldas", "Doctorado/PhD", "1"),
("2021", "Esmeraldas", "Grado", "118"),
("2021", "Esmeraldas", "Posgrado", "110"),
("2021", "Ibarra", "Grado", "3"),
("2021", "Ibarra", "Grado", "119"),
("2021", "Ibarra", "Posgrado", "125"),
("2021", "Quito", "Grado", "20"),
("2021", "Quito", "Grado", "452"),
("2021", "Quito", "Posgrado", "74"),
("2021", "Santo Domingo", "Grado", "3"),
("2021", "Santo Domingo", "Grado", "34"),
("2021", "Santo Domingo", "Posgrado", "33"),
("2021", "Nacional", "Grado", "32"),
("2021", "Nacional", "Doctorado/PhD", "1"),
("2021", "Nacional", "Grado", "825"),
("2021", "Nacional", "Posgrado", "476"),
]
datos_Posgrado=[
("2023", "Ambato", "No", "224"),
("2023", "Ambato", "Si", "61"),
("2023", "Ambato", "(en blanco)", "37"),
("2023", "Esmeraldas", "No", "45"),
("2023", "Esmeraldas", "Si", "4"),
("2023", "Esmeraldas", "(en blanco)", "4"),
("2023", "Ibarra", "No", "179"),
("2023", "Ibarra", "Si", "28"),
("2023", "Ibarra", "(en blanco)", "18"),
("2023", "Quito", "No", "621"),
("2023", "Quito", "Si", "167"),
("2023", "Quito", "(en blanco)", "120"),
("2023", "Santo Domingo", "No", "48"),
("2023", "Santo Domingo", "Si", "15"),
("2023", "Santo Domingo", "(en blanco)", "10"),
("2023", "Manabí", "No", "141"),
("2023", "Manabí", "Si", "37"),
("2023", "Manabí", "(en blanco)", "36"),
("2023", "Nacional", "No", "1258"),
("2023", "Nacional", "Si", "312"),
("2023", "Nacional", "(en blanco)", "225"),
("2022", "Ambato", "No", "134"),
("2022", "Ambato", "Si", "41"),
("2022", "Esmeraldas", "No", "100"),
("2022", "Esmeraldas", "Si", "13"),
("2022", "Ibarra", "No", "220"),
("2022", "Ibarra", "Si", "36"),
("2022", "Quito", "No", "658"),
("2022", "Quito", "Si", "231"),
("2022", "Santo Domingo", "No", "122"),
("2022", "Santo Domingo", "Si", "16"),
("2022", "Manabí", "No", "11"),
("2022", "Manabí", "Si", "5"),
("2022", "Nacional", "No", "1245"),
("2022", "Nacional", "Si", "342"),
("2021", "Ambato", "No", "199"),
("2021", "Ambato", "Si", "41"),
("2021", "Esmeraldas", "No", "206"),
("2021", "Esmeraldas", "Si", "25"),
("2021", "Ibarra", "No", "217"),
("2021", "Ibarra", "Si", "30"),
("2021", "Quito", "No", "418"),
("2021", "Quito", "Si", "128"),
("2021", "Santo Domingo", "No", "59"),
("2021", "Santo Domingo", "Si", "11"),
("2021", "Nacional", "No", "1099"),
("2021", "Nacional", "Si", "235"),
]
datos_capacitacion=[
("2023", "Ambato", "No", "116"),
("2023", "Ambato", "Sí", "206"),
("2023", "Esmeraldas", "No", "21"),
("2023", "Esmeraldas", "Sí", "32"),
("2023", "Ibarra", "No", "93"),
("2023", "Ibarra", "Sí", "132"),
("2023", "Quito", "No", "288"),
("2023", "Quito", "Sí", "620"),
("2023", "Santo Domingo", "No", "26"),
("2023", "Santo Domingo", "Sí", "47"),
("2023", "Manabí", "No", "89"),
("2023", "Manabí", "Sí", "125"),
("2023", "Nacional", "No", "633"),
("2023", "Nacional", "Sí", "1162"),
]
datos_emprededores=[
("2023", "Ambato", "34"),
("2023", "Esmeraldas", "4"),
("2023", "Ibarra", "37"),
("2023", "Quito", "59"),
("2023", "Santo Domingo", "3"),
("2023", "Manabí", "16"),
("2023", "Nacional", "153"),
("2022", "Ambato", "30"),
("2022", "Esmeraldas", "11"),
("2022", "Ibarra", "67"),
("2022", "Quito", "97"),
("2022", "Santo Domingo", "5"),
("2022", "Manabí", "3"),
("2022", "Nacional", "213"),
("2021", "Ambato", "19"),
("2021", "Esmeraldas", "1"),
("2021", "Ibarra", "9"),
("2021", "Quito", "11"),
("2021", "Nacional", "40"),
]
    # [TODOS LOS DATOS PERMANECEN IGUALES HASTA EL FINAL DE datos_sector]
# Crear DataFrames con la columna de año

# Crear DataFrames (los datos deben ser definidos previamente)
df_graduados = pd.DataFrame(datos_graduados, columns=["Año", "SEDES", "Graduados"])
df_empleo = pd.DataFrame(datos_empleo, columns=["Año", "SEDES", "Conseguir empleo", "Participantes"])
df_situacion = pd.DataFrame(datos_situacion, columns=["Año", "SEDES", "Situación laboral", "Participantes"])
df_sector = pd.DataFrame(datos_sector, columns=["Año", "SEDES", "Sector", "Participantes"])
df_ocupacion = pd.DataFrame(datos_ocupacion, columns=["Año", "SEDES", "Ocupación", "Participantes"])
df_nivelsalarial = pd.DataFrame(datos_nivelsalario, columns=["Año", "SEDES", "Nivel Salarial", "Participantes"])
df_relacion = pd.DataFrame(datos_relacion, columns=["Año", "SEDES", "Relación formación-empleo", "Participantes"])
df_nivelalcanzado = pd.DataFrame(datos_nivelalcanzado, columns=["Año", "SEDES", "Nivel de estudios", "Participantes"])
df_posgrado = pd.DataFrame(datos_Posgrado, columns=["Año", "SEDES", "Posgrado", "Participantes"])
df_capacitacion = pd.DataFrame(datos_capacitacion, columns=["Año", "SEDES", "Capacitación", "Participantes"])
df_emprendedores = pd.DataFrame(datos_emprededores, columns=["Año", "SEDES", "Participantes"])
df_emprendedores["Categoría"] = "Emprendedores"

# Convertir a numérico
df_graduados["Graduados"] = pd.to_numeric(df_graduados["Graduados"], errors="coerce")
df_empleo["Participantes"] = pd.to_numeric(df_empleo["Participantes"], errors="coerce")
df_situacion["Participantes"] = pd.to_numeric(df_situacion["Participantes"], errors="coerce")
df_sector["Participantes"] = pd.to_numeric(df_sector["Participantes"], errors="coerce")
df_ocupacion["Participantes"] = pd.to_numeric(df_ocupacion["Participantes"], errors="coerce")
df_nivelsalarial["Participantes"] = pd.to_numeric(df_nivelsalarial["Participantes"], errors="coerce")
df_relacion["Participantes"] = pd.to_numeric(df_relacion["Participantes"], errors="coerce")
df_nivelalcanzado["Participantes"] = pd.to_numeric(df_nivelalcanzado["Participantes"], errors="coerce")
df_posgrado["Participantes"] = pd.to_numeric(df_posgrado["Participantes"], errors="coerce")
df_capacitacion["Participantes"] = pd.to_numeric(df_capacitacion["Participantes"], errors="coerce")
df_emprendedores["Participantes"] = pd.to_numeric(df_emprendedores["Participantes"], errors="coerce")

# Obtener listas únicas
años_disponibles = sorted(df_graduados["Año"].unique().tolist())
sedes_disponibles = sorted([s for s in df_empleo["SEDES"].unique().tolist()], key=lambda x: x.lower())

# App
app = dash.Dash(__name__)
server = app.server

# Función para crear tablas
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

# Layout de la aplicación
app.layout = html.Div(style={
    "fontFamily": "Arial, sans-serif",
    "padding": "20px",
    "maxWidth": "1400px",
    "margin": "0 auto",
    "backgroundColor": "#f8f9fa"
}, children=[
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
        
        html.Div(style={"flex": "2", "minWidth": "250px"}, children=[
            html.Label("Seleccionar Sede:", style={"fontWeight": "bold", "marginBottom": "5px"}),
            dcc.Dropdown(
                id="selector-sedes",
                options=[{"label": sede, "value": sede} for sede in sedes_disponibles],
                value=sedes_disponibles[0] if sedes_disponibles else None,
                clearable=False
            )
        ]),
        
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
    
    # Tarjeta de graduados
    html.Div(id="graduados-numero", style={
        "padding": "20px",
        "backgroundColor": "white",
        "borderRadius": "8px",
        "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
        "marginBottom": "30px",
        "textAlign": "center"
    }),
    
    # Primera fila de tablas
    html.Div(style={
        "display": "flex",
        "flexWrap": "wrap",
        "gap": "15px",
        "marginBottom": "30px"
    }, children=[
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Tiempo Conseguir Primer Empleo", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-empleo")
        ]),
        
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Situación Laboral Actual", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-situacion")
        ]),
        
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
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
        ]),
    ]),
    
    # Segunda fila de tablas
    html.Div(style={
        "display": "flex",
        "flexWrap": "wrap",
        "gap": "15px",
        "marginBottom": "30px"
    }, children=[
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Nivel Salarial", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-nivelsalarial")
        ]),
        
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Relación Formación-Empleo", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-relacion")
        ]),
        
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Nivel de Estudios Alcanzado", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-nivelalcanzado")
        ]),
        
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Estudian Posgrado", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-posgrado")
        ]),
    ]),
    
    # Tercera fila de tablas
    html.Div(style={
        "display": "flex",
        "flexWrap": "wrap",
        "gap": "15px",
        "marginBottom": "30px"
    }, children=[
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Capacitación", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-capacitacion")
        ]),
        
        html.Div(style={"flex": "1", "minWidth": "300px"}, children=[
            html.H2("Emprendedores", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"
            }),
            html.Div(id="tabla-emprendedores")
        ]),
    ])
])

# Callbacks
@app.callback(
    Output("selector-anio", "value"),
    Input("boton-todos-anios", "n_clicks"),
    prevent_initial_call=True
)
def manejar_boton_todos_anios(n_clicks):
    return "Todos"

@app.callback(
    Output("graduados-numero", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_numero_graduados(anio_seleccionado, sede_seleccionada):
    df_filtrado = df_graduados[df_graduados["SEDES"] == sede_seleccionada]
    
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
    
    df_filtrado = df_filtrado[df_filtrado["Año"] == anio_seleccionado]
    
    if not df_filtrado.empty:
        resultado = df_filtrado["Graduados"].iloc[0]
    else:
        resultado = None
    
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

# Callbacks para las tablas principales
@app.callback(Output("tabla-empleo", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_empleo(anio, sede): 
    return crear_tabla_con_multianios(df_empleo, "Conseguir empleo", "Participantes", anio, sede)

@app.callback(Output("tabla-situacion", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_situacion(anio, sede): 
    return crear_tabla_con_multianios(df_situacion, "Situación laboral", "Participantes", anio, sede)

@app.callback(Output("tabla-sector", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_sector(anio, sede): 
    return crear_tabla_con_multianios(df_sector, "Sector", "Participantes", anio, sede)

@app.callback(Output("tabla-ocupacion", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_ocupacion(anio, sede): 
    return crear_tabla_con_multianios(df_ocupacion, "Ocupación", "Participantes", anio, sede)

@app.callback(Output("tabla-nivelsalarial", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_nivelsalarial(anio, sede): 
    return crear_tabla_con_multianios(df_nivelsalarial, "Nivel Salarial", "Participantes", anio, sede)

@app.callback(Output("tabla-relacion", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_relacion(anio, sede): 
    mapeo_descripciones = {
        "1": "1 (Poco relacionado)",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5 (Muy relacionado)",
        "No aplica": "No aplica",
        "(en blanco)": "No aplica"
    }
    df_relacion_mapeado = df_relacion.copy()
    df_relacion_mapeado["Relación formación-empleo"] = df_relacion_mapeado["Relación formación-empleo"].map(
        lambda x: mapeo_descripciones.get(x, x)
    )
    return crear_tabla_con_multianios(df_relacion_mapeado, "Relación formación-empleo", "Participantes", anio, sede)

# Callbacks para las nuevas tablas
@app.callback(Output("tabla-nivelalcanzado", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_nivelalcanzado(anio, sede): 
    return crear_tabla_con_multianios(df_nivelalcanzado, "Nivel de estudios", "Participantes", anio, sede)

@app.callback(Output("tabla-posgrado", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_posgrado(anio, sede): 
    return crear_tabla_con_multianios(df_posgrado, "Posgrado", "Participantes", anio, sede)

@app.callback(Output("tabla-capacitacion", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_capacitacion(anio, sede): 
    return crear_tabla_con_multianios(df_capacitacion, "Capacitación", "Participantes", anio, sede)

@app.callback(Output("tabla-emprendedores", "children"), [Input("selector-anio", "value"), Input("selector-sedes", "value")])
def actualizar_tabla_emprendedores(anio, sede): 
    return crear_tabla_con_multianios(df_emprendedores, "Categoría", "Participantes", anio, sede)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run(host='0.0.0.0', port=port, debug=True)