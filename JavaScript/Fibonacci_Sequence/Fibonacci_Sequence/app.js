// This one is very slow but it works!!!
//This is a basic Fibonacci Sequence and a
//tree formula to see how high the sequence can 
//go from adding each leaf on the branch all the 
//way to the root.

//const fib = (n) => {
//    if (n <= 2) return 1;
//    return fib(n - 1) + fib(n - 2);
//}
//console.log(fib(10)); // 55
//console.log(fib(20)); // 6765
//console.log(fib(30)); // 832040
//console.log(fib(40)); // 102334155
//above is as high as my computer could run before getting to slow.

//Holy Cow!! 
//below will be a memoization try to get even higher numbers.
//Was done by taking each number and remebering groups of repeating branches.
//using Node.js memo in this sequence remembers the stored value of node in the tree 
//without going down the sub tree of the right side.

const fib2 = (n, memo = {}) => {
    if (n in memo) return memo[n];
    if (n <= 2) return 1;
    memo[n] = fib2(n - 1, memo) + fib2(n - 2, memo);
    return memo[n];
}
console.log(fib2(45)) // 1134903170
console.log(fib2(50)) // 12586269025
console.log(fib2(55)) // 139583862445
console.log(fib2(60)) // 1548008755920
console.log(fib2(65)) // 17167680177565
console.log(fib2(70)) // 190392490709135
console.log(fib2(1000)) // 4.346655768693743e+208 

function Pause(i) {
    if (i == 5) return;
    setTimeout(function ()
    {
        writeNext(i + 1);

    }, 5000);
}

Pause(1);