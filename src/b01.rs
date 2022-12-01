use std::collections::BinaryHeap;

const day: &str = "01";

pub fn run() -> i64 {
    let inp = std::fs::read_to_string(format!("input/{}.txt", day)).expect("Error reading input");

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
