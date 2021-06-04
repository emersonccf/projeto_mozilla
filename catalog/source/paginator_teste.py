from django.core.paginator import Paginator

objects = ['emerson','sofia', 'francisco', 'bruno', 'allan', 'carla', 'pedro']

p = Paginator(objects, 2) # cria um paginador (que tem num de páginas (num_pages), qtd elementos no paginador (count) )
paginas = p.page_range # intervalo de paginas ex. range(1,4)

for pag in paginas:
    pagina = p.page(pag) # pagina atual
    if not pagina.has_previous() and pagina.number == 1:
        print(" "*11, pagina.number,"Próxima ->")
    elif pagina.has_next():
        print("<- Anterior",pagina.number,"Próxima ->")
    else:
        print("<- Anterior", pagina.number)




    