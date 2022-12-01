const day: &str = "01";

pub fn run() -> i64 {
    let inp = std::fs::read_to_string(format!("input/{}.txt", day)).expect("Error reading input");
    
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
