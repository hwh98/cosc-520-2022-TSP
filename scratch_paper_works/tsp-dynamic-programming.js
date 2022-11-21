/**
 *  Author's Name: Hongda Li
 *  This code is made for COSP 2022 Winter Term 1, final project. And I am Hongda Li. I don't like javascript, but I guess
 *  I can deal with it. 
 */

const { isNull } = require("lodash");

var TSPDPModule = (function (){
    
    console.log("Dynamic Programming module is being loaded");
    const THIS_MODULE = "[TSPDModule]: "
    var DYNAMIC_TABLE = {};
    var BEST_SPANNING_PATH = null;
    var BEST_SPATH_LENGTH;
    var VERBOSE = false;

    
    function println(str=null)
    {
        if (str === null && VERBOSE) console.log(str);
    }

    /**
     * 
     * @param {number} a : An array of uniqe elements to choose from. 
     * @param {number} k : The size of the subsets that we want to choose from. 
     * @yield {number}: A finger print encoding the choice of the subset. 
     */
    function *k_combinatorics(n, k)
    {
        if (!Number.isInteger(n) || !Number.isInteger(k)) throw "n, k must be integer to use k_combinatorics fxn. ";
        if (n <- k) throw " k > n and we have ${k} > ${n}. ";
        function *k_combinatorics_recur(a, k, start_at, already_chosen)
        {
            if (k == 0) {
                yield already_chosen;
                return;
            }
            n = a.length
            for (let I = start_at; I <= n - k; I++)
            {
                already_chosen.push(a[I]);
                yield* k_combinatorics_recur(a, k - 1, I + 1, already_chosen);
                already_chosen.pop();
            }
        }
        yield* k_combinatorics_recur(Array.from(Array(n).keys()), k, 0, []);
    }

    
    /*
    * A class that can generate finger prints for all the subsets of a given set. The set has to be a set and not some 
    * kind of multi-set. 
    * with size n
    */
    class SubsetGenerator
    {
        /**
         * The construct for the subsets generator. give it an array with unique elements as the set to take the s
         * subsets from. 
         */
        constructor(elements)
        {
            if (!Array.isArray(elements))
            {
                throw `arguments has to be type of array. `
            }
            this.n = elements.length;
            this.elements = elements;
        }

        /**
         * Get a generator for the subset of size k for the given sets. 
         */
        *k_get(k)
        {
            let g = k_combinatorics(this.n, k);
            for (let item = g.next(); !item.done; item = g.next())
            {
                let res_arr = item.value.map(x => this.elements[x]);
                yield res_arr;
            }
        }
        
    };

    /**
     * Perform the dynamic programming approach to figure out the solution for a directed graph with edge weight assignment. 
     * `c` is the maps that maps a 2 elements 
     * @param {object} c: c is a maps that maps an array of 2 elements to their edge costs. 
     */
    function tsp_dynamic(c)
    {
        if (!(typeof c === 'object')) throw `${THIS_MODULE} Please at least pass an object for the function: tsp_dynamic.`

        DYNAMIC_TABLE = {}; // clear previous results! 
        function construct_pair_distances()
        {
            for (const [k, v] of Object.entries(c)) 
            {
                if (k !== v) DYNAMIC_TABLE[[k, v]] = c[[k, v]];
            }
        }
        let all_vertices = new Set(Object.keys(c));
        
        

        
    }; 


//======================================================================================================================
    /**
     *  Doing some tests on the subset generator. 
     */
    function simple_test1()
    {   
        let g = k_combinatorics(5, 3);
        let s = 0;
        for (let item = g.next(); !item.done; item = g.next())
        {
            s++;
        }
        console.assert(s == 10, "simple_test1 failed. ");
        console.log("Simple Test 1 passed. ");
    }

    /**
     * A test function for unit testing. 
     */
    function simple_test2()
    {
        let gen = new SubsetGenerator([1, 2, 3, 4, 5]);
        gen = gen.k_get(3);
        let s = 0;
        for (let item = gen.next(); !item.done; item = gen.next())
        {
            s++;
        }
        console.assert(s == 10, "simple_test2 failed. ");
        console.log("Simple Test 1 passed.");
    }

    function dynamic_programming_test() 
    {

    }

    /**
     *  A function that runs the test or run the setup for things. 
     */
    function must_run(){
        simple_test1(); simple_test2();
        return;
    }

    must_run();
    
    // export this module. 
    return {
        DYNAMIC_TABLE: BEST_SPANNING_PATH, 
        BEST_SPANNING_PATH: BEST_SPANNING_PATH
    }

})();