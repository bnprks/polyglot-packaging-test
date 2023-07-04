

test_that("R_add works", {
    expect_identical(add_R(1, 2), 3L)
})

test_that("R_message works", {
    expect_identical(message_R(), "Hello from C++!")
})