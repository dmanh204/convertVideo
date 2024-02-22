import subprocess

def video_to_binary(input_video_path):
    # Use ffmpeg to read the video and output binary data
    command = [
        'F:/TaiLieuHocTap/sip/StreamCipher/convertvideo-main/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg',  # Adjust this path to the location of your ffmpeg executable
        '-i', input_video_path,
        '-f', 'image2pipe',
        '-vcodec', 'h264',
        '-pix_fmt', 'rgb24',
        '-'
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    if process.returncode != 0:
        raise Exception(f"FFmpeg error: {err.decode()}")

    return out

def binary_to_binary_string(binary_data):
    # Convert binary data to a string of binary digits
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    return binary_string

def save_to_file(binary_string, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(binary_string)

def main():
    input_video_path = 'F:/TaiLieuHocTap/sip/StreamCipher/convertvideo-main/big_buck_bunny_720p_2mb.mp4'
    output_file_path = 'video_binary.txt'

    try:
        binary_data = video_to_binary(input_video_path)
        binary_string = binary_to_binary_string(binary_data)

        # Save to file
        save_to_file(binary_string, output_file_path)
        print(f"Binary data saved to {output_file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
