# Heuristic function necessary to test algoritm
def heuristic(estat):
    if estat == [4,3,2,1]: return 6
    elif estat == [4,3,1,2]: return 5
    elif estat == [4,1,3,2]: return 4
    elif estat == [1,4,3,2]: return 3
    elif estat == [1,3,4,2]: return 2
    elif estat == [1,3,2,4]: return 1
    elif estat == [1,2,3,4]: return 0
    else: return 10

def tl_estrategia_Astar (nodes_a_expandir, nous_nodes_a_expandir):
    unio = nous_nodes_a_expandir + nodes_a_expandir
    return quicksort(selecciona_estimacio(unio),unio)

quicksort([10, 4, 3],['n1', 'n2', 'n3']) # ['n3', 'n2', 'n1']

def selecciona_estimacio (unio_nodes):
    return mapcar(lambda node: caddr(cdddr(node)), unio_nodes)

def quicksort (per_ordenar, elems):
    if not elems:
        return []
    pivot = car(per_ordenar)
    elemp = car(elems)
    petits = selecciona_menorigual(pivot, cdr(per_ordenar), cdr(elems))
    grans = selecciona_major(pivot, cdr(per_ordenar), cdr(elems))
    return quicksort(selecciona_estimacio(petits),petits) + 
            cons(elemp, quicksort(selecciona_estimacio(grans),grans))

def selecciona_menorigual (pivot, per_ordenar, elems):
    if not per_ordenar:
        return []
    ll = selecciona_menorigual(pivot,cdr(per_ordenar),cdr(elems))
    if car(per_ordenar) <= pivot:
        return cons(car(elems),ll)
    return ll
 
def selecciona_major (pivot, per_ordenar, elems):
    if not per_ordenar:
        return []
    ll = selecciona_major(pivot,cdr(per_ordenar),cdr(elems))
    if car(per_ordenar) > pivot:
        return cons(car(elems),ll)
    return ll

def cerca_Astar (problema):
    return fer_cerca(problema, tl_estrategia_Astar)

def problema_cercaAstar():
    tl_ops = tl_operadors()
    def aux_func(info_node_pare, estat, operador):
        estat_pare = car(info_node_pare)
        g          = caadr(info_node_pare)
        g_mes_pare = g + 1
        g_mes_h    = g_mes_pare + heuristic(estat)
        return [g_mes_pare, g_mes_h]
    estat_inicial = [4,3,2,1]
    check_estat_final = lambda estat: estat == [1,2,3,4]
    return [tl_ops, aux_func, estat_inicial,
            check_estat_final,
            lambda estat: [0, heuristic(estat)

cerca_Astar(problema_cercaAstar())
['id', 'ic', 'ie', 'ic', 'id', 'ic']
