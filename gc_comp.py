def gc_comp(dna):
    """Calculates the GC percentage of a DNA string."""
    # Convert to uppercase to handle 'g' and 'c' as well
    dna = dna.upper()
    
    g_count = dna.count('G')
    c_count = dna.count('C')
    
    # Calculate the ratio
    if len(dna) == 0:
        return 0.0
        
    gc_total = g_count + c_count
    return (gc_total / len(dna)) * 100

# Get input from the user
sequence = input("Enter a DNA sequence: ")

# Calculate and report
percentage = gc_comp(sequence)
print(f"The GC composition is: {percentage:.2f}%")