/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {

    // for(let i =0;i<nums.length; i++)
    // {
    //     for(let j =i+1; j< nums.length; j++)
    //         {
    //             console.log(i,j)
    //             if(nums[i] + nums[j] === target){
    //                 return [i, j]
    //             }
    //             else
    //                 continue

    //         }
    // }

    // var myMap = new Map();
    // var keyObj = {};
    // nums.forEach((element, index) => {
    //     let compliment = target-element;
    //     if(myMap.has(compliment)){
    //         return ([myMap.get(compliment),index] )
    //     }
    //     myMap.set(element, index)
    // });
    // console.log(myMap)

    let myMap = new Map();
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (myMap.has(complement)) {
            return ([myMap.get(complement), i]);
        }
        myMap.set(nums[i], i);

    }
}
