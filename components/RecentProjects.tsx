"use client";

import { FaLocationArrow } from "react-icons/fa6";

import { projects } from "@/data";
import { PinContainer } from "./ui/Pin";

const RecentProjects = () => {
  return (
    <div className="py-20">
      <h1 className="heading">
        Our project's{" "}
        <span className="text-purple">components</span>
      </h1>
      <div className="form-container">
    <iframe
      src="https://docs.google.com/forms/d/e/1FAIpQLSdCX3ZcrrsdomOTXLcnphzurhDrb_29ZKeW2Z74L5Qgn_UANg/viewform?embedded=true"
      width="640"
      height="800"
      title="Google Form"
    >
      Loading…
    </iframe>
  </div>
    </div>
  );
};

export default RecentProjects;
