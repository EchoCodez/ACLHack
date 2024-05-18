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
      src="https://forms.gle/cQqm7aLhQQmr8uCw7/viewform?embedded=true"
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
