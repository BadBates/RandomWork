const depthFirstPrint = (graph, source) => {
    const stack = [source];

    while (stack.length > 0) {
        const current = stack.pop();
        console.log(current);

        for (let neighbor of graph[current]) {
            stack.push(neighbor);
        }
    }
};

//a,c,e,b,d,f repeating 
//this was the out come of this graph with all of
//them connected to at least one other node. 
const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: ['b'],
    f: ['a']
}

function Pause(i) {
    if (i == 5) return;
    setTimeout(function () {
        writeNext(i + 1);
    }, 5000);
}

depthFirstPrint(graph, 'a');
Pause(1);