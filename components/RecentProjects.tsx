"use client";

import { FaLocationArrow } from "react-icons/fa6";
import { projects } from "@/data";
import { PinContainer } from "./ui/Pin";

const RecentProjects = () => {
  return (
    <div>
      <div className="py-20 my">
        <h1 className="heading">
          Analyze your{" "}
          <span className="text-purple my-4">conversation</span>
        </h1>
      </div>
      <div className="form-container flex justify-center items-center mt-10">
        <iframe
          src="https://docs.google.com/forms/d/e/1FAIpQLSdCX3ZcrrsdomOTXLcnphzurhDrb_29ZKeW2Z74L5Qgn_UANg/viewform?embedded=true"
          width="640"
          height="787"
        >
          Loading…
        </iframe>
      </div>
    </div>
  );
};

export default RecentProjects;
