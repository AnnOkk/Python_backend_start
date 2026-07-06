


class Fibonacci:
    def __init__(self,quantity):
        self.quantity = quantity
    def __iter__(self):
        prev = 1
        prev_prev = 1
        counter = 1
        while counter <= self.quantity:
            if counter <= 2:
                yield 1
            else:
                current = prev
                prev = prev + prev_prev
                prev_prev = current
                yield prev
            counter += 1







#
# export function Fibonacci(quantity) {
#     // TODO: Implement Fibonacci sequence calculation
#     // [1] = 1 [2] = 1 [n] = [n-1] + [n-2]
#     // 1, 1, 2, 3, 5, 8, 13, 21
#     this.quantity = quantity;
#     this[Symbol.iterator] =  () => {
#         return {
#             prev: 1,
#             prevPrev: 1,
#             counter: 1,
#             next: function () {
#                 if (this.counter <= quantity) {
#                     if (this.counter++ <= 2) {
#                         return {done: false, value: 1};
#                     }
#                     const current = this.prev;
#                     this.prev = this.prev + this.prevPrev;
#                     this.prevPrev = current;
#                     return {done: false, value: this.prev};
#                 } else {
#                     return {done: true}
#                 }
#             }
#         }
#     }
# }

