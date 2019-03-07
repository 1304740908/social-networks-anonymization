import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    g = nx.fast_gnp_random_graph(10,0.09)
    g = g.to_undirected()
    return g


def draw_graph(g):
    nx.draw(g, pos=nx.spring_layout(g), node_size=50, font_size=6, font_color='w', arrowsize=3)
    plt.draw()
    plt.savefig('img.png', dpi=500)
    plt.close()


def compute_degree(g):
    degree = g.degree()

    total_degree = 0
    max_degree = 0
    min_degree = g.number_of_nodes()
    for node,degree_node in degree:
        total_degree = total_degree + degree_node
        if (degree_node > max_degree):
            max_degree = degree_node
        if (degree_node < min_degree):
            min_degree = degree_node
        #print(node, degree_node)
    
    print('\nTotal Degree: ', total_degree/g.number_of_nodes())
    print('Max Degree: ', max_degree)
    print('Min Degree: ', min_degree)


def print_measurements(g):
    print('Number of nodes:', g.number_of_nodes())
    print('Number of edges:', g.number_of_edges())
    print('Number of self-loops:', g.number_of_selfloops())
    compute_degree(g)

    #print(g.degree(['1','2','3']))



if __name__ == '__main__':
    g = create_graph()
    print_measurements(g)
    #draw_graph(g)