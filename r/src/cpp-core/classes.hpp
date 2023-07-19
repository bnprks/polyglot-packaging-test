#include <string>

namespace Animals {

/**
 * @brief An animal base class
 * 
 */
class Animal {
  public:
    /**
     * @brief Get a message about the animal
     * 
     * @return std::string The message
     */
    virtual std::string message() = 0;
    std::string publicMember; /**< Some description of a public member */

  protected:
    
    /**
     * @brief A protected method
     * 
     * @param a Random parameter
     * @return int The return integer
     */
    int protectedMethod(int a) const { return 4; }
    int protectedMember; /**< Some description of a protected member */
};

/**
 * @brief A Dog class
 * 
 * Some longer information about dogs.
 */
class Dog : public Animal {
  public:
    std::string message() { return "Dog"; }
    /**
     * @brief Get the dog breed
     * 
     * @return std::string The breed
     */
    virtual std::string breed() const = 0;
};

/**
 * @brief A Corgi class
 * 
 * Corgis are the cutest dog breed.
 * 
 */
class Corgi : public Dog {
  public:
    std::string breed() const override { return "Corgi"; }
};

} // namespace Animals