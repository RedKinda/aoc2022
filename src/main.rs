mod a01;
use a01::run;
const DAY: &str = "01";

fn main() {
    let inp = std::fs::read_to_string(format!("input/{}.txt", DAY)).unwrap();
    let result = run(inp);
    println!("Result day {}: {}", DAY, result);
}
