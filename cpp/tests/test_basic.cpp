#include <gtest/gtest.h>

#include <add.hpp>
#include <message.hpp>

using namespace Polyglot;

TEST(Basic, Add) {
    ASSERT_EQ(add(1,2), 3);
}

TEST(Basic, Message) {
    ASSERT_EQ(message(), "Hello from C++!");
}