def main() :
    # Assignment 3
    print("="*50)
    print("Assignment 3:")
    print()  
    y_inital = 5
    x_inital = 1
    approx = 1.499 # decimals of .5 and prone to rounding errors.
    func = func_1    
    
    # PART 1
    print("(1)\n")
    step_size = 0.1
    run(func, x_inital, y_inital, step_size, approx)
    # PART 2
    print("(2)\n")
    step_size = 0.05
    func = func_1
    run(func, x_inital, y_inital, step_size, approx)

    # Assignment 5
    print("="*50)
    print("Assignment 5:")
    print()  
    y_inital = 0
    x_inital = 0
    approx = 0.499 # decimals of .5 and prone to rounding errors.
    func = func_2    
    
    # PART 1
    print("(1)\n")
    step_size = 0.1
    run(func, x_inital, y_inital, step_size, approx)
    # PART 2
    print("(2)\n")
    step_size = 0.05
    run(func, x_inital, y_inital, step_size, approx)


def func_1(x,y) : return 2*x -3*y +1    
def func_2(x,y) : return 1 + y**2
def run(func, x, y, step, approx) :
    x_vals = [] # Stores all X values leading up to specified approximation  
    y_vals = [] # Stores all Y values calculated.
    
    # initialize default values.
    x_vals.append(x)
    y_vals.append(y)

    # Start calculations.
    euler_method(func, x, y, x_vals, y_vals, 
                        step, approx)
    # Display data.
    output(x_vals,y_vals)


def euler_method(func, x, y, x_results,y_results,step_size,approx) :
    if not x < approx : return # base case
    
    y = y + step_size * func(x,y) # update Y value.
    y_results.append(y) # Store current Y value.
    x += step_size # incerment X by step size.
    x_results.append(x) # Store current X value.
    
    # Repeat.
    euler_method(func,x,y,x_results,y_results,step_size,approx)

# Formats and outputs N,X,Y in a table like format.
def output(x_vals, y_vals) :
    print("%2s  %18s  %18s"%("N","X","Y"))
    print("_"*50)
    for i in range(0,len(x_vals),1) :
        print("%2d  %18.2f  %18.4f"%(i,x_vals[i],  y_vals[i]))
        print("_"*50)
    print()
    print()

main()
