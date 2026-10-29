# Chapter 10 Programming Projects - Instructor Answer Key

Each script uses only what Chapter 10 teaches: `print()`, strings, comments, and simple arithmetic.
All 16 were run in Python 3 and produce the output shown in the comments/guide below.

## General checks (every project)
- Script runs with no SyntaxError or run-time error
- Each project is in its own `.py` file in the student's repo directory
- Uses `print()` correctly (parentheses, matching quotes, no stray indentation)
- Includes a comment at the top (Chapter 10 introduces comments)

## Per-project notes

| # | Project | What to look for | Reference output / note |
|---|---------|------------------|-------------------------|
| 1 | Greeting | Any greeting, any language | `¡Hola, mundo!` |
| 2 | Sum 1..10 | Computed by Python, not hard-typed `55` | `55` |
| 3 | Product 1..10 | Uses `*`, not `x` | `3628800` |
| 4 | Balance, years 1-3 | 1000 at 5%: 1050, 1102.5, 1157.625 | Values must be correct; extra decimals from floating point (e.g. 1102.5000000000002) are acceptable. Variables are fine if students already know them. |
| 5 | Name in box | Box drawn with `+ - \|`, name centered, sides align | 3 print lines |
| 6 | Name in large letters | Each letter built from `*`, letters line up across all rows | Student's own name; every row the same height |
| 7 | Face | Original face, not a copy of the textbook | Needs to be "similar to but different from" |
| 8 | Mondrian | Rectangles outlined with `- \|` and filled with `@@@`/`:::` blocks | Open-ended; check rows align |
| 9 | House | Must match the picture **exactly**, including spacing | Compare character by character |
| 10 | Animal greeting | Animal plus speech bubble, different from textbook | Backslashes must be doubled (`\\`) in a normal string; a single `\` can cause errors or warnings. Good teaching moment. |
| 11 | Three items | Three separate `print` calls, three lines | |
| 12 | Poem | Poem of their choice | Watch for copyrighted poems; Dickinson / cummings are suggested |
| 13 | US flag | Uses `*` and `=` | Open-ended; stars in a corner field, stripes alongside/below |
| 14 | Birthdays | Two aligned columns | Alignment done with spaces inside strings |
| 15 | Sales tax | Five states, header matching the sample | Rates vary by source and change; accept any plausible researched values |
| 16 | Phrases | Two columns, all four phrases translated | Accept any language; check columns align |

## Common student errors (from Section 10.8)
- `Print(...)` or `PRINT(...)`: Python is case sensitive
- Missing closing quote: syntax error
- Missing quotes around text: `print(Hello)` is a syntax error / NameError
- Inconsistent indentation before a `print`
- Single backslashes in ASCII art (projects 7 and 10)
