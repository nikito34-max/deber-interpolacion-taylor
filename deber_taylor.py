"""Deber de interpolación y Taylor. Nikolai Ortega, GR1CC.
Ejecutar: python3 deber_taylor.py
Genera las tres gráficas y los resultados de las secciones programadas.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def taylor_sin(x, n):
    """Maclaurin de seno hasta el grado impar n; escalar o ndarray."""
    if not isinstance(n, (int, np.integer)) or n < 1 or n % 2 == 0:
        raise ValueError('n debe ser un entero positivo impar')
    x = np.asarray(x, dtype=float)
    termino = x.copy()
    suma = termino.copy()
    for k in range((n - 1) // 2):
        termino = termino * (-x * x / ((2*k + 2) * (2*k + 3)))
        suma = suma + termino
    return suma.item() if suma.ndim == 0 else suma


def serie_geometrica(x, N):
    """S_N: N+1 términos, desde k=0 hasta k=N; grado 2N."""
    if not isinstance(N, (int, np.integer)) or N < 0:
        raise ValueError('N debe ser un entero no negativo')
    x = np.asarray(x, dtype=float)
    termino = np.ones_like(x)
    suma = termino.copy()
    for _ in range(N):
        termino = termino * (-x * x)
        suma = suma + termino
    return suma.item() if suma.ndim == 0 else suma


def taylor_exp(x, n=100):
    termino = 1.0
    suma = termino
    mayor = abs(termino)
    for k in range(1, n + 1):
        termino *= x / k
        suma += termino
        mayor = max(mayor, abs(termino))
    return suma, mayor


def main():
    salida = Path(__file__).resolve().parent
    plt.rcParams.update({'font.size': 11, 'figure.figsize': (10, 6)})
    x = np.linspace(-2*np.pi, 2*np.pi, 2001)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), 'k', linewidth=2.5, label='sin(x)')
    for n in [1, 3, 5, 7, 9]:
        ax.plot(x, taylor_sin(x, n), label=f'P{n}(x)', linestyle='--')
    ax.set(xlim=(-2*np.pi, 2*np.pi), ylim=(-2, 2), xlabel='x (radianes)',
           ylabel='Valor', title='Seno y polinomios de Maclaurin')
    ax.grid(alpha=.25); ax.legend(ncol=3); fig.tight_layout()
    fig.savefig(salida/'01_seno_taylor.png', dpi=180); plt.close(fig)
    grados = list(range(1, 22, 2))
    errores = []
    for a, b in [(-np.pi, np.pi), (-np.pi/4, np.pi/4)]:
        malla = np.linspace(a, b, 2001)
        errores.append([float(np.max(np.abs(np.sin(malla)-taylor_sin(malla, n))))
                        for n in grados])
    fig, ax = plt.subplots()
    for err, etiqueta in zip(errores, ['[-π, π]', '[-π/4, π/4]']):
        ax.semilogy(grados, err, 'o-', label=etiqueta)
    ax.axhline(1e-6, color='gray', linestyle='--', label='Tolerancia 10⁻⁶')
    ax.set(xlabel='Grado impar n', ylabel='Error máximo (escala logarítmica)',
           title='Error máximo del polinomio de seno')
    ax.set_xticks(grados); ax.grid(alpha=.25, which='both'); ax.legend()
    fig.tight_layout(); fig.savefig(salida/'02_errores_seno.png', dpi=180); plt.close(fig)
    x = np.linspace(-1.5, 1.5, 2001)
    fig, ax = plt.subplots()
    ax.plot(x, 1/(1+x*x), 'k', linewidth=2.5, label='1/(1+x²)')
    for N in [2, 5, 10, 20]:
        ax.plot(x, serie_geometrica(x, N), '--', label=f'S{N} (grado {2*N})')
    ax.set(xlim=(-1.5, 1.5), ylim=(-.5, 1.5), xlabel='x', ylabel='Valor',
           title='Serie geométrica y región de convergencia')
    ax.axvline(-1, color='gray', linewidth=.8); ax.axvline(1, color='gray', linewidth=.8)
    ax.grid(alpha=.25); ax.legend(ncol=2); fig.tight_layout()
    fig.savefig(salida/'03_serie_geometrica.png', dpi=180); plt.close(fig)
    negativo, mayor = taylor_exp(-20)
    positivo, _ = taylor_exp(20)
    lineas = [f'P9(pi) = {taylor_sin(np.pi, 9):.15g}',
              f'Grados mínimos = {[next(n for n,e in zip(grados,err) if e < 1e-6) for err in errores]}',
              f'S40(0.9) = {serie_geometrica(.9,40):.15g}',
              f'S40(1.1) = {serie_geometrica(1.1,40):.15g}',
              f'P100(-20) = {negativo:.17g}',
              f'math.exp(-20) = {math.exp(-20):.17g}',
              f'Mayor término absoluto = {mayor:.17g}',
              f'1/P100(20) = {1/positivo:.17g}',
              '\nGrado | Error [-pi,pi] | Error [-pi/4,pi/4]']
    lineas += [f'{n:2d} | {a:.12e} | {b:.12e}' for n,a,b in zip(grados,*errores)]
    texto = '\n'.join(lineas)
    print(texto)
    (salida/'resultados.txt').write_text(texto+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
