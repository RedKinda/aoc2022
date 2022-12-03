use bitvec::prelude::*;
use std::collections::HashSet;

#[inline]
fn char_to_val(c: &char) -> u8 {
    if *c > 'Z' {
        *c as u8 - b'a' + 1
    } else {
        *c as u8 - b'A' + 27
    }
}

pub fn run(inp: &str) -> i64 {
    inp.lines()
        .map(|line| {
            let mut bitarr: BitArr!(for 53) = BitArray::ZERO;
            let line_len = line.len();

            unsafe {
                line.chars().take(line_len / 2).for_each(|c| {
                    bitarr.set_unchecked(char_to_val(&c) as usize, true);
                });

                line.chars()
                    .skip(line_len / 2)
                    .find_map(|c| {
                        let val = char_to_val(&c) as usize;
                        if *bitarr.get_unchecked(val) {
                            Some(val)
                        } else {
                            None
                        }
                    })
                    .unwrap() as i64
            }
        })
        .sum::<i64>()
        .into()
}

// naive implementation
pub fn run_naive(inp: &str) -> i64 {
    let mut priority_sum = 0;

    for line in inp.lines() {
        let line_len = line.len();

        let first_half = line[0..line_len / 2].chars();
        let second_half = line[line_len / 2..].chars();

        let a: HashSet<char> = HashSet::from_iter(first_half);
        let b: HashSet<char> = HashSet::from_iter(second_half);

        let intersection: Vec<&char> = a.intersection(&b).collect();
        let overlap = intersection[0];

        let priority = if overlap.is_lowercase() {
            *overlap as u8 - b'a' + 1
        } else {
            *overlap as u8 - b'A' + 27
        };

        priority_sum += priority as i64;
    }

    priority_sum
}
