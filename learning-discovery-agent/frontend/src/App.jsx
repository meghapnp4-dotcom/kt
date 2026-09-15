import { useEffect, useState } from "react";

export default function App() {
  const [courses, setCourses] = useState([]);
  const [query, setQuery] = useState("");
  const [enrollments, setEnrollments] = useState([]);

  const API_URL = import.meta.env.VITE_API_URL || "/api";

  const buildUrl = (path) => `${API_URL.replace(/\/$/, "")}${path}`;

  useEffect(() => {
    loadCourses();
  }, []);

  const loadCourses = async () => {
    try {
      const response = await fetch(buildUrl("/courses"));
      const data = await response.json();
      setCourses(data);
    } catch (error) {
      console.error("Failed to load courses:", error);
    }
  };

  const loadPopularCourses = async () => {
    try {
      const response = await fetch(buildUrl("/popular"));
      const data = await response.json();
      setCourses(data);
    } catch (error) {
      console.error("Failed to load popular courses:", error);
    }
  };

  const enroll = (course) => {
    const exists = enrollments.find(
      (item) => item.learningId === course.learningId
    );

    if (!exists) {
      setEnrollments([...enrollments, course]);
    }
  };

  const unenroll = (id) => {
    setEnrollments(
      enrollments.filter(
        (item) => item.learningId !== id
      )
    );
  };

  const filteredCourses = courses.filter((course) =>
    course.title?.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-slate-100 p-8">
      <h1 className="text-5xl font-bold mb-8">
        Learning Discovery Agent
      </h1>

      <div className="bg-white rounded-2xl shadow p-6 mb-8">
        <input
          type="text"
          placeholder="Search courses..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-full border p-3 rounded-lg"
        />

        <div className="flex gap-4 mt-4">
          <button
            onClick={loadCourses}
            className="bg-blue-600 text-white px-4 py-2 rounded"
          >
            All Courses
          </button>

          <button
            onClick={loadPopularCourses}
            className="bg-green-600 text-white px-4 py-2 rounded"
          >
            Popular Courses
          </button>
        </div>
      </div>

      <div className="bg-white rounded-2xl shadow p-6 mb-8">
        <h2 className="text-3xl font-bold mb-6">
          Courses ({filteredCourses.length})
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {filteredCourses.map((course) => (
            <div
              key={course.learningId}
              className="border rounded-xl p-4 shadow-sm"
            >
              <h3 className="text-xl font-bold mb-2">
                {course.title}
              </h3>

              <p>
                <strong>ID:</strong> {course.learningId}
              </p>

              <p>
                <strong>Provider:</strong> {course.provider}
              </p>

              <p>
                <strong>Level:</strong> {course.level}
              </p>

              <p>
                <strong>Type:</strong> {course.learningType}
              </p>

              <p>
                <strong>Duration:</strong> {course.durationHours} hrs
              </p>

              <p>
                <strong>Rating:</strong> {course.rating}
              </p>

              <p>
                <strong>Enrollments:</strong> {course.enrollmentCount}
              </p>

              <button
                onClick={() => enroll(course)}
                className="mt-4 bg-blue-600 text-white px-4 py-2 rounded"
              >
                Enroll
              </button>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-white rounded-2xl shadow p-6">
        <h2 className="text-3xl font-bold mb-4">
          My Enrollments
        </h2>

        {enrollments.length === 0 ? (
          <p>No enrollments yet</p>
        ) : (
          enrollments.map((course) => (
            <div
              key={course.learningId}
              className="border rounded-lg p-4 mb-3"
            >
              <h3 className="font-bold">
                {course.title}
              </h3>

              <p>{course.learningId}</p>

              <button
                onClick={() => unenroll(course.learningId)}
                className="bg-red-600 text-white px-4 py-2 rounded mt-2"
              >
                Unenroll
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  );
}