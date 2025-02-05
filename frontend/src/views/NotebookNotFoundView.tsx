/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import Footer from "../components/Footer";
import HomeNavBar from "../components/HomeNavBar";

export default function NotebookNotFoundView() {
  return (
    <div className="App">
      <HomeNavBar isSitePublic={true} username={""} />
      <div
        style={{
          width: "100%",
          maxWidth: "500px",
          padding: "15px",
          margin: "0 auto",
        }}
      >
        <h3>Notebook not found</h3>
        <p>
          We can't find your notebook. Please double check the URL address and permissions.
        </p>
      </div>
      <Footer />
    </div>
  );
}
