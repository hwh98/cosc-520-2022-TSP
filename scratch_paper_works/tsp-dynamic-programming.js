(()=>{
    console.log("Dynamic Programming module is being loaded")
    let DYNAMIC_TABLE = {};

    /**
     * A generator for subsets. It generates the subsets of size k in a sized n set, and the number it returns represents 
     * binary instruction to generate the subsets. for examples, given n = 3, k = 2, it means to choose from a sets of 3 
     * for all subsets of size 2, it will return: 
     * - 11 -> the first one, the second one, but not the third one.
     * - 101 -> the first and last one and not the second one. 
     * - 110 -> The last 2 but not the third one. 
     * @{param} {number} n : The size of the whole se that we want to choose the subsets from. 
     * @{param} {number} k : The size of the subsets that we want to choose from. 
     * @{param} {number} [off_set]: This is a recursive parameter that you should not touch. 
     * @{yield} {number}: A finger print encoding the choice of the subset. 
     */
    function *k_combinatorics(n, k, off_set=0)
    {
        if (!(Number.isInteger(n) && Number.isInteger(k))) throw `n: ${n}; k: ${k} has to be integers.`
        if (k > n) throw `n < k with ${n} < ${k}, combinator failed.`;
        if (k == 1)
        {
            for (let I = off_set; I < n; I++)
            {
                yield 1 << I;
            }
            return // Terminates base case
        }
        for (let I = off_set; I <= n - k; I++) 
        {   
            sub_itr = k_combinatorics(n, k - 1, off_set=I + 1);
            for (let itm = sub_itr.next(); !itm.done; itm = sub_itr.next())
            {
                yield (1 << I) + itm.value;
            }
        }
    }

    /*
    * A class that can generate finger prints for all the subsets of a given set
    * with size n
    */
    class SubSetGenerator
    {
        constructor(n, elements)
        {
            if (!Number.isInteger(n) || n <= 0)
            {
                throw `Number n=${n} is not an integer of it's positive`
            }
            if (!Array.isArray(elements))
            {
                throw `arguments has to be type of array. `
            }
            this.n = n;
            this.elements = elements;
        }

        /**
         * Get a generator for the subset of size k for the given sets. 
         */
        k_get(k)
        {
            let fingerprint_gen = k_combinatorics(this.n, k);
            for (let fg = fingerprint_gen.value; !fingerprint_gen.done; fg = fingerprint_gen.next())
            {
                for (let I = 0; I < this.n; I++)
                {
                    
                }
            }
        }
        
        select(the_set)
        {

            return null
        }
    };



})();