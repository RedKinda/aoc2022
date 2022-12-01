pub mod a01;
pub use a01::run;
pub const DAY: &str = "01";

pub fn run_dry() {
    let inp = std::fs::read_to_string(format!("input/{}.txt", DAY)).unwrap();
    let result = run(inp.as_str());
    println!("Result day {}: {}", DAY, result);
}
