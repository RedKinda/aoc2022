pub fn run(inp: &str) -> i64 {
    let mut res = 0;

    for line in inp.lines() {
        let parts = line.split(",").collect::<Vec<_>>();
        let parts_a = parts[0].split("-").collect::<Vec<_>>();
        let parts_b = parts[1].split("-").collect::<Vec<_>>();
        let aa = parts_a[0].parse::<i64>().unwrap();
        let ab = parts_a[1].parse::<i64>().unwrap();
        let ba = parts_b[0].parse::<i64>().unwrap();
        let bb = parts_b[1].parse::<i64>().unwrap();
        if (ba <= ab && aa <= bb) || (aa <= bb && ba <= ab) {
            res += 1;
        }
    }

    res
}
