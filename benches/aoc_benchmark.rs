use aoc::{run, DAY};
use criterion::{black_box, criterion_group, criterion_main, Criterion};

pub fn criterion_benchmark(c: &mut Criterion) {
    let inp = std::fs::read_to_string(format!("input/{}.txt", DAY)).unwrap();

    c.bench_function(format!("aoc day {}", DAY).as_str(), |b| {
        b.iter(|| run(black_box(inp.as_str())))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
