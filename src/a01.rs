pub fn run(inp: &str) -> i64 {
    inp.split("\n\n")
        .map(|x| {
            x.lines()
                .map(|num| num.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .max()
        .unwrap()
        .into()
}
