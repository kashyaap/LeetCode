/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

/**
Learned about appending stuff to likedList
Plus, do as the questions says, if you start infering then you might face problems with the test cases.
What happened with me was that, I was reversing the final added sum, but that was a problem, the question specifically said add the reversed nos. 
1000 cases passed with that solution with the no being reversed but others failed. Plus the fact that var can't store values more than 
Value. 21024 - 2971, or approximately 1.7976931348623157E+308 so we needed to change everything to bigInt. 
**/
var addTwoNumbers = function(l1, l2) {
    
    var varOfLinkedList = function(l1) {
    let sum = BigInt(0);
    let power = BigInt(0);
    
    while (l1 != null) {
        let val = BigInt(l1.val);
        sum = (val * BigInt(10) ** power) + sum;
        l1 = l1.next;
        power += BigInt(1);
    }
    return sum;
}
    
    var numberToLinkedList = function(num) {
        num = BigInt(num);

        if (num === BigInt(0)) return new ListNode(0);

        let dummyHead = new ListNode(0);
        let current = dummyHead;

        while (num > 0) {
            let digit = num % BigInt(10); 
            current.next = new ListNode(Number(digit));
            current = current.next;
            num = num / BigInt(10);
        }
    return dummyHead.next;
};
    let l1sum = varOfLinkedList(l1)
    let l2sum = varOfLinkedList(l2)
    return(numberToLinkedList(l1sum + l2sum)); 
    
};
