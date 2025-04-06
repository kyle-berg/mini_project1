# Data Comm Mini Project - dvrouting.py
# Kyle Berg

import csv

node_cnt = 11  # Number of nodes in the network

# Initialize the Distance Table Header
distance_table_header = list()

def print_distance_table(distance_table, distance_table_header):
    """
    Print the distance table in a formatted manner.
    :param distance_table: The distance table to print
    :param distance_table_header: The distance table header to print
    """
    print("\nDistance Table:")
    print(" ", end="")
    print("  | ".join(map(str, distance_table_header)) + "   |")
    print("----------------")
    for row in distance_table:
        if (int(row[0]) < 10):
            print(" ", end="")
        print(" | ".join(map(str, row))+ " |")
    print("--------------------")

def print_routing_table(routing_table, routing_table_header):
    """
    Print the distance table in a formatted manner.
    :param distance_table: The distance table to print
    :param distance_table_header: The distance table header to print
    """
    print("\nRouting Table:")
    print(" | ".join(map(str, routing_table_header)))
    print("----------------------------------")
    for row in routing_table:
        if (int(row[0]) < 10):
            print(" ", end="")
        print("    | ".join(map(str, row)))
    print("----------------------------------")


def main():
    # Read Node_Init.csv to initialize the distance table
    with open('Node_Init.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Read the first row to initialize the distance table structure
        # The first row contains the headers which are the node numbers
        first_row = next(csv_reader)
        neighbor_cnt = (len(first_row) - 1)
        distance_table = [([f"{i}"] + ([float('inf')] * neighbor_cnt)) for i in range(1, node_cnt+1)]
        distance_table_header = list(map(int, first_row))

        # Initialize the distance table with the distance values from the second row
        # The second row contains the initial distances from the node to its neighbors
        second_row = next(csv_reader)
        for i in range(1, len(second_row)):
            distance_table[distance_table_header[i]-1][i] = float(second_row[i])

    # Print Distance Table
    print_distance_table(distance_table, distance_table_header)

    # Initialize routing table
    routing_table_header = ["Dest", "NextHop", "Minimum Distance"]
    routing_table = [([f"{i}"] + ([float('inf')] * 2)) for i in range(1, node_cnt+1)]

    # Update routing table based on the distance table
    for i in range(len(distance_table)):
        min_distance = float('inf')
        next_hop = None
        for j in range(1, len(distance_table[i])):
            if distance_table[i][j] < min_distance:
                min_distance = distance_table[i][j]
                next_hop = distance_table_header[j]

        # Update the routing table for the current node
        routing_table[i][1] = float(next_hop) if next_hop is not None else float('inf')
        routing_table[i][2] = min_distance if min_distance != float('inf') else float('inf')

    # Print Routing Table
    print_routing_table(routing_table, routing_table_header)

    # Print Distance Vectors
    print("\nDistance Vectors to send:")
    for i in range(len(distance_table)):
        for j in range(1, len(distance_table[i])):
            if distance_table[i][j] != float('inf'):
                print(f"[{distance_table_header[0]}, {distance_table_header[j]}, {distance_table[i][j]}]")
    
    print("\n-----------ROUND 1-----------")

    


    
if __name__ == '__main__':
    main()