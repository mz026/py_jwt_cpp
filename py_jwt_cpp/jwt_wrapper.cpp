#include <pybind11/pybind11.h>
#include <pybind11/stl.h>   // For Python-C++ STL conversions
#include <jwt-cpp/jwt.h>    // Include jwt-cpp
#include <string>
#include <map>

namespace py = pybind11;

std::string encode(
    const std::map<std::string, std::string>& claims,
    const std::string& private_key,
    const std::map<std::string, std::string>& headers = {} // Default empty map
) {
    auto token = jwt::create();

    // Add claims from the input map to the JWT payload
    for (const auto& [claim, value] : claims) {
        token.set_payload_claim(claim, jwt::claim(value));
    }

    // Add custom headers if provided
    for (const auto& [key, value] : headers) {
        token.set_header_claim(key, jwt::claim(value));
    }

    // Sign the JWT using RS256
    return token.sign(jwt::algorithm::rs256("", private_key, "", ""));
}

// pybind11 module
PYBIND11_MODULE(jwt_cpp, m) {
    m.def(
        "cpp_encode",
        &encode,
        py::arg("payload"),          // Map for claims
        py::arg("private_key"),      // Private key for signing
        py::arg("headers") = std::map<std::string, std::string>{}, // Default header
        "Encode a JWT with given payload, RS256 private key, and optional headers."
    );
}
