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
