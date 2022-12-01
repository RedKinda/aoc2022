pub fn run(inp: &str) -> i64 {
    inp.split("\n\n")
        .map(|x| {
            x.lines()
                .map(|num| num.parse::<i64>().unwrap())
                .sum::<i64>()
        })
        .max()
        .unwrap()
        .into()
}
