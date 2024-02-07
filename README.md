# Analisis de algoritmos

## Soluciones reto 1

Dada una lista de numeros y un target $x$ imprima todos los pares unicos de esa lista que sumen $x$. Mas formalmente: Imprima todas las parejas del array $a[]$ tal que $1 \le i < j \le n$ y $a_i+a_j=x$ donde $n$ es el tamaño del arreglo.

### Naive solution $\mathcal{O}(n^2)$

Recorra todas las parejas del array y determine cuales parejas suman $x$. Esta solucion va a ser usada para el Stress Testing.

La complejidad de la solucion es $\mathcal{O}(n^2)$

### Binary search solution $\mathcal{O}(n \log n)$

Denote que cada par debe ser unico y para cada $a_i$ se debe buscar un elemento $a_j$ tal que la suma de $x$. Si se tiene el arreglo ordenado, denote la siguiente observación para el array $a = [1, 4, 5, 6]$ y $x = 5$.

$$\underbrace{1,}_{a_i} \underbrace{4, 5, 6}_{\text{search for }a_j}$$

En realidad para cada $i$ que se fije, se debe buscar en el array restante $a_j$. Se busca el elemento se resulte de la ecuacion: $x-a_i = a_j$. Para buscar el elemento se puede hacer **binary search** en el array restante.

La complejidad de la solución es $\mathcal{O}(n\log n)$ teniendo en cuenta que hay que ordenar el array.

**Esta solución no sería valida si hay elementos repetidos en el arreglo**.

### Array lockup solution $\Theta(n)$

Teniendo en cuenta la solucion anterior, sabemos que para cada $a_i$ hay que buscar $|x-a_i| = a_j$ para poder formar la pareja. Se puede referenciar $a_j$ como la posición de un arreglo que va a hacer de diccionario o mapa en el caso de C++. Formalmente se tiene el array $\mathrm{cnt}[]$ el cual en $\mathrm{cnt}_{a_j}$ se va a almacenar la cantidad de elementos que necesitan de $a_j$ para formar un par. Cuando se vaya recorriendo los elementos, se verifica si el elemento esta siendo pedido por algún otro elemento del arreglo, si es así, se puede revertir la ecuación para obtener el otro miembro de la pareja.

El comportamiento asintotico de esta solución es $\Theta(n)$ ya que siempre hay que recorrer el arreglo para obtener la solucion. Siguiendo la definición formal del comportamiento asíntotico de $\Theta$.

- $f(n) = \Theta(g(n))$ o $f \asymp g$ si $f=\mathcal{O}(g)$ y $f=\Omega(g)$ ($f$ crece a la misma velocidad que $g$).

**Esta solución funciona unicamente para valores de $a_i$ positivos y depende de los limites del problema.**

En caso de que se tuviera valores negativos, entonces se tendría que usar un `map` o alguna estractura que pudiera referenciar $a_i$ como llave o indice. Sin embargo, con estructuras como estas las operaciones se hacen en $\mathcal{O}(\log n)$ entonces la complejidad quedaría igual que la anterior solución (**Dicha solucion si permitiría numeros repetidos**).

### Map Solution $\mathcal{O}(n \log n)$

Esta es la solucion discutida al final de la anterior solucion, sin embargo, esta solucion utiliza una estructura adicional para poder llevar los indices de los enteros negativos.

Dependiendo de la estructura, se define la complejidad, ya que si el acceso a los elementos de la estructura se hace en $\mathcal{O}(\log n)$ entonces la complejidad sería $\mathcal{O}(n \log n)$ pero si la estructura accede a los elementos de manera constante (Como el array en la solucion anterior $\mathcal{O}(1)$) entonces la complejidad en dicho caso si quedaría $\Theta(n)$.
