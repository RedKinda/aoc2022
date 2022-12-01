use std::collections::BinaryHeap;

pub fn run(inp: &str) -> i64 {
    // take and sum top 3 numbers
    BinaryHeap::from_iter(inp.split("\n\n").map(|x| {
        x.lines()
            .map(|num| num.parse::<u32>().unwrap())
            .sum::<u32>()
    }))
    .iter()
    .take(3)
    .sum::<u32>()
    .into()
}
