# Deber de interpolación y polinomios de Taylor
Nikolai Ortega - GR1CC

## Ejecución
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 deber_taylor.py
```
El script genera tres PNG y resultados.txt en su propia carpeta.

## Entrega en Policlase
- RESPUESTAS_EN_ORDEN.txt: respuestas de las 22 preguntas, en orden.
- DESARROLLO_A_MANO.md: guía para escribir y comprobar los dos ejercicios.
- Pregunta 9: hasta tres fotos reales de tus hojas.
- Pregunta 13: 01_seno_taylor.png y 02_errores_seno.png.
- Pregunta 17: 03_serie_geometrica.png.
- Pregunta 22: enlace a tu repositorio público y las dos funciones solicitadas.

## GitHub
Crea un repositorio público con los archivos del proyecto. Si usas GitHub CLI
y ya te autenticaste, desde esta carpeta ejecuta:
```bash
git init
git branch -M main
git add .
git commit -m "Deber de interpolacion y polinomios de Taylor"
gh repo create deber-interpolacion-taylor --public --source=. --remote=origin --push
```
Si ese nombre ya existe, elige otro. Copia la URL real que devuelva GitHub;
el paquete no afirma que el repositorio esté publicado.
