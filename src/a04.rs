pub fn run(inp: &str) -> i64 {
    inp.as_bytes()
        .split(|&b| b == b'\n')
        .filter(|s| !s.is_empty())
        .filter(|line| {
            let mut nums: [u32; 4] = [0, 0, 0, 0];
            let mut ind = 0;

            unsafe {
                line.iter().for_each(|c| {
                    if *c < b'0' {
                        ind += 1;
                    } else {
                        *nums.get_unchecked_mut(ind) = nums.get_unchecked(ind) * 10 + *c as u32;
                    }
                });
            }

            let aa = nums[0];
            let ab = nums[1];
            let ba = nums[2];
            let bb = nums[3];
            (aa <= ba && ba <= bb && bb <= ab) || (ba <= aa && aa <= ab && ab <= bb)
        })
        .count() as i64
}

pub fn run_slow(inp: &str) -> i64 {
    let mut res = 0;

    for line in inp.lines() {
        let parts = line.split(",").collect::<Vec<_>>();
        let parts_a = parts[0].split("-").collect::<Vec<_>>();
        let parts_b = parts[1].split("-").collect::<Vec<_>>();
        let aa = parts_a[0].parse::<i64>().unwrap();
        let ab = parts_a[1].parse::<i64>().unwrap();
        let ba = parts_b[0].parse::<i64>().unwrap();
        let bb = parts_b[1].parse::<i64>().unwrap();
        if (aa <= ba && ba <= bb && bb <= ab) || (ba <= aa && aa <= ab && ab <= bb) {
            res += 1;
        }
    }

    res
}
