#![allow(dead_code)]
use std::mem;

struct Point {
    x: f64,
    y: f64 }

fn origin() -> Point 
{ 
    Point{x: 0.0, y: 0.0 }
}

fn main() {
    let p1 = origin(); //Saves a Point structure to the stack
    let p2 = Box::new(origin()); //Saves a pointer/memory address to a Point Structure
                                //The Pointer Structure itself is saved to the heap
    
    println!("p1 takes up {} bytes", mem::size_of_val(&p1)); 
    println!("p2 takes up {} bytes", mem::size_of_val(&p2)); 
    
    
}


	//Option<T>
	let x = 3.0;
	let y = 2.0;
	//returns Some(z) or None
	let result:Option<f64> = 
		if y != 0.0 {Some(x/y)} else { None };
	println!("{:?}", result);

	match result {

		Some(z) => println!("{}/{} = {}", x,y,z),
		None => println!("Cannot divide by 0")
	}
	
	//if let
	if let Some(z) = result { println!("z={}", z); }

    //Example of Practical Use: Vectors
    
    let mut v = Vec::new();
    v.push(0);
    v.push(1);
    let index = 0;
    println!("V[0] = {}", v[index]);
    
    match v.get(3) {
        Some(x) => println!("V[3] = {}", x),
        None => println!("Error, no such element")
    
    }
    
}
