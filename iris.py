null=0
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMPCUbPYBZjNjNeL50oEGXo",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sraochintalapudi/irisflowerclassification/blob/main/MLProject1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hyiT2KnzHT4k",
        "outputId": "b5ee6596-230f-4df3-fafb-49559d5cc639"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "This is my first Machine Learning Project\n"
          ]
        }
      ],
      "source": [
        "print(\"This is my first Machine Learning Project\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd"
      ],
      "metadata": {
        "id": "QnwjMzGjHrFT"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "iris=pd.read_csv(\"/content/sample_data/iris.csv\")"
      ],
      "metadata": {
        "id": "MI0hMwb8Ip9R"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "iris"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 647
        },
        "id": "qOaJ7tPSKLAi",
        "outputId": "5154b0f6-bde4-4b20-e5bc-00c08167d8da"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     sepal_length  sepal_width  petal_length   petal_width           class\n",
              "0             5.1          3.5           1.4           0.2     iris_setosa\n",
              "1             4.9          3.0           1.4           0.2     iris_setosa\n",
              "2             4.7          3.2           1.3           0.2     iris_setosa\n",
              "3             4.6          3.1           1.5           0.2     iris_setosa\n",
              "4             5.0          3.6           1.4           0.2     iris_setosa\n",
              "..            ...          ...           ...           ...             ...\n",
              "145           6.7          3.0           5.2           2.3  iris_virginica\n",
              "146           6.3          2.5           5.0           1.9  iris_virginica\n",
              "147           6.5          3.0           5.2           2.0  iris_virginica\n",
              "148           6.2          3.4           5.4           2.3  iris_virginica\n",
              "149           5.9          3.0           5.1           1.8  iris_virginica\n",
              "\n",
              "[150 rows x 5 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-916ef9ec-f19c-49bf-bb56-49358cba00af\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "      <th>class</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.6</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>145</th>\n",
              "      <td>6.7</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.3</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>146</th>\n",
              "      <td>6.3</td>\n",
              "      <td>2.5</td>\n",
              "      <td>5.0</td>\n",
              "      <td>1.9</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>147</th>\n",
              "      <td>6.5</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.0</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>148</th>\n",
              "      <td>6.2</td>\n",
              "      <td>3.4</td>\n",
              "      <td>5.4</td>\n",
              "      <td>2.3</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>149</th>\n",
              "      <td>5.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>1.8</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>150 rows × 5 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-916ef9ec-f19c-49bf-bb56-49358cba00af')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-916ef9ec-f19c-49bf-bb56-49358cba00af button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-916ef9ec-f19c-49bf-bb56-49358cba00af');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=iris.drop(columns=['class'])\n",
        "y=iris['class']\n",
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)"
      ],
      "metadata": {
        "id": "cvAaMLGTKVX-"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn import neighbors\n",
        "classifier=neighbors.KNeighborsClassifier()"
      ],
      "metadata": {
        "id": "i6QbFwyWLRg9"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "classifier.fit(x_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-Nlls9QLMOD2",
        "outputId": "921267c4-eb91-4091-91e9-7f05f5f7ed69"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "KNeighborsClassifier()"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "predictions=classifier.predict(x_test)"
      ],
      "metadata": {
        "id": "6IS9lPEDMcql"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score\n",
        "print(accuracy_score(y_test,predictions)*100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4evRx6kiMtZM",
        "outputId": "4bfe2bd5-f578-4ac1-af25-c4caedadec5d"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "96.66666666666667\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn import tree\n",
        "dstreeclassifier=tree.DecisionTreeClassifier()\n",
        "dstreeclassifier.fit(x_train,y_train)\n",
        "dstreepredictions=dstreeclassifier.predict(x_test)\n",
        "print(accuracy_score(y_test,dstreepredictions)*100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gnzFjdUFPjQP",
        "outputId": "4318c879-0808-4919-a269-53f6e7007077"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "93.33333333333333\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "fig=plt.figure()\n",
        "fig.suptitle(\"Algorithm Comparision\")\n",
        "names=['KNN','Decision Tree']\n",
        "result=[96.66,93.33]\n",
        "plt.bar(names,result)\n",
        "plt.xlabel(\"Algorithm\")\n",
        "plt.ylabel(\"Accuracy\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 326
        },
        "id": "zLcsoW8pV92u",
        "outputId": "aaa42aa0-c535-40e7-fb9d-ce75b13a23e2"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0, 0.5, 'Accuracy')"
            ]
          },
          "metadata": {},
          "execution_count": 25
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}
