# Regressao-linear-simples


A regressão linear simples é uma ferramenta estatística onde dados um conjunto de dados x e y, o objetivo é encontrar a melhor equação de reta que descreve aquele conjunto de dados. Para aproximar  essa reta aos dados, pode-se seguir a equação abaixo para aproximar os coeficientes $\beta_0$ e $\beta_1$:

<br>

$$
\large
\begin{cases}
\hat{\beta}_1=\frac{\sum_{i=1}^n (x_i- \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{\sigma_{xy}}{\sigma_{xx}} = \frac{covar(x, y)}{var(x)}\\
\hat{\beta}_0= \bar{y}-\hat{\beta_1}\bar{x}
\end{cases}
$$

<br>

Onde:
- **Covariância** ou variância conjunta, que indica o grau de interdependência entre duas variáveis;
- **Variância** é uam medida de o quão disperso está os dados, ou seja o quão distante está cada valor desse conjunto do valor médio;

A função `linear_regression` recebe duas listas x e y e devolve os valores dos coeficientes $\beta_0$, $\beta_1$ e exibe o gráfico da regressão.

![regres](https://user-images.githubusercontent.com/45486420/210632041-69610e48-2d0d-43a9-9880-ac741a20a055.png)
